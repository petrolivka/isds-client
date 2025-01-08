from pathlib import Path
from typing import Optional, Dict, Any
from zeep import Client, Settings, exceptions
from zeep.transports import Transport
import requests
import base64


class ISDSError(Exception):
    """Base exception for ISDS client errors."""

    pass


class ISDSClient:
    """Client for Czech Data Box Information System (ISDS)."""

    def __init__(
        self,
        username: str,
        password: str,
        production: bool = False,
        wsdl_dir: Optional[Path] = None,
    ):
        """Initialize ISDS client.

        Args:
            username: Login username
            password: Login password
            production: If True, use production environment, otherwise test
            wsdl_dir: Directory containing WSDL files (defaults to ./wsdl)
        """
        self.username = username
        self.password = password
        self.production = production

        # Set base URLs based on environment
        if production:
            self.base_url = "https://ws1.mojedatovaschranka.cz/DS"
        else:
            self.base_url = "https://ws1.czebox.cz/DS"

        # Set WSDL directory
        self.wsdl_dir = wsdl_dir or Path(__file__).parent / "wsdl"

        # Initialize services
        self._clients: Dict[str, Client] = {}
        self._init_services()

    def _init_services(self):
        """Initialize SOAP clients for each service."""
        # Configure transport with basic auth
        session = requests.Session()

        # Set up Basic Auth header
        auth_string = self._basic_auth(self.username, self.password)
        session.headers.update(
            {
                "Authorization": auth_string,
                "Content-Type": "text/xml;charset=UTF-8",
            }
        )

        transport = Transport(session=session)

        # Configure Zeep settings with defaults
        settings = Settings()

        # Initialize clients for each service with their endpoints
        service_files = {
            "dm_operations": ("dm_operations.wsdl", "dx"),
            "dm_info": ("dm_info.wsdl", "dx"),
            "db_search": ("db_search.wsdl", "df"),
            "db_access": ("db_access.wsdl", "db"),
            "db_manipulations": ("db_manipulations.wsdl", "dbm"),
        }

        for service_name, (wsdl_file, endpoint) in service_files.items():
            wsdl_path = self.wsdl_dir / wsdl_file
            if wsdl_path.exists():
                try:
                    # Create the client with the local WSDL file
                    client = Client(
                        wsdl=str(wsdl_path), transport=transport, settings=settings
                    )

                    # Update the service address to use the correct base URL and endpoint
                    service_url = f"{self.base_url}/{endpoint}"
                    service = client.create_service(
                        list(client.wsdl.bindings.values())[0].name, service_url
                    )

                    self._clients[service_name] = service
                except Exception as e:
                    raise ISDSError(
                        f"Failed to initialize {service_name} client: {str(e)}"
                    )
            else:
                raise FileNotFoundError(f"WSDL file not found: {wsdl_path}")

    def _basic_auth(self, username: str, password: str) -> str:
        """Helper method to create basic auth string."""
        auth_string = base64.b64encode(f"{username}:{password}".encode()).decode()
        return f"Basic {auth_string}"

    def _call_service(self, service_name: str, operation_name: str, **kwargs) -> Any:
        """Helper method to call SOAP service with error handling.

        Args:
            service_name: Name of the service to call
            operation_name: Name of the operation to call
            **kwargs: Arguments to pass to the operation

        Returns:
            The response from the service

        Raises:
            ISDSError: If there is an error calling the service
        """
        service = self._clients.get(service_name)
        if not service:
            raise ISDSError(f"{service_name} service not initialized")

        try:
            operation = getattr(service, operation_name)
            response = operation(**kwargs)

            if response is None:
                raise ISDSError(f"No response received from {operation_name}")

            return response
        except exceptions.Fault as e:
            fault_detail = getattr(e, "detail", None)
            if fault_detail:
                if isinstance(fault_detail, bytes):
                    fault_detail = fault_detail.decode("utf-8")
                raise ISDSError(f"SOAP fault: {fault_detail}")
            raise ISDSError(f"SOAP fault: {str(e)}")
        except Exception as e:
            raise ISDSError(f"Error calling {operation_name}: {str(e)}")

    def get_message_info(self, message_id: str):
        """Get information about a specific message.

        Args:
            message_id: ID of the message to retrieve
        """
        return self._call_service("dm_info", "GetDeliveryInfo", dmID=message_id)

    def create_message(self, recipient_id: str, subject: str, content: str, **kwargs):
        """Create and send a new message.

        Args:
            recipient_id: ID of the recipient's data box
            subject: Subject of the message
            content: Content of the message
            **kwargs: Additional message parameters
        """
        params = {
            "dmEnvelope": {
                "dbIDRecipient": recipient_id,
                "dmAnnotation": subject,
            },
            "dmContent": content,
            **kwargs,
        }
        return self._call_service("dm_operations", "CreateMessage", **params)

    def search_data_box(self, query: str):
        """Search for data boxes.

        Args:
            query: Search query
        """
        return self._call_service("db_search", "FindDataBox", searchText=query)

    def get_delivery_info(self, message_id: str):
        """Get delivery information for a message.

        Args:
            message_id: ID of the message to retrieve delivery info for
        """
        return self._call_service("dm_info", "GetDeliveryInfo", dmID=message_id)
