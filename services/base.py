import logging
from pathlib import Path
from typing import Any
from zeep import Client, Settings, exceptions
from zeep.transports import Transport
import requests
import base64
from zeep.helpers import serialize_object
from zeep.plugins import HistoryPlugin


class ISDSError(Exception):
    """Base exception for ISDS client errors."""

    pass


class BaseService:
    """Base class for ISDS services."""

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        wsdl_dir: Path,
        wsdl_filename: str,
        endpoint: str,
        debug: bool = False,
    ):
        """Initialize the service.

        Args:
            username: Login username
            password: Password
            base_url: Base URL of the ISDS service
            wsdl_dir: Directory containing WSDL files
            wsdl_filename: Name of the WSDL file for this service
            endpoint: Service endpoint (e.g., 'dx', 'df', etc.)
        """
        self.username = username
        self.password = password
        self.base_url = base_url
        self.wsdl_path = wsdl_dir / wsdl_filename
        self.endpoint = endpoint
        self.history = HistoryPlugin()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG if debug else logging.INFO)
        self.debug = debug
        self.service = self._init_service()

    def _init_service(self):
        """Initialize the SOAP service."""
        if not self.wsdl_path.exists():
            raise FileNotFoundError(f"WSDL file not found: {self.wsdl_path}")

        # Configure transport with basic auth
        session = requests.Session()
        auth_string = self._basic_auth(self.username, self.password)
        session.headers.update(
            {"Authorization": auth_string, "Content-Type": "text/xml;charset=UTF-8"}
        )
        transport = Transport(session=session)

        try:
            # Create the client with the local WSDL file
            client = Client(
                wsdl=str(self.wsdl_path),
                transport=transport,
                settings=Settings(),
                plugins=[self.history],
            )

            # Update the service address to use the correct base URL and endpoint
            service_url = f"{self.base_url}/{self.endpoint}"
            return client.create_service(
                list(client.wsdl.bindings.values())[0].name, service_url
            )
        except Exception as e:
            raise ISDSError(f"Failed to initialize service: {str(e)}")

    def _basic_auth(self, username: str, password: str) -> str:
        """Create basic auth header value."""
        auth_string = base64.b64encode(f"{username}:{password}".encode()).decode()
        return f"Basic {auth_string}"

    def _call(self, operation_name: str, **kwargs) -> Any:
        """Call a service operation with error handling.

        Args:
            operation_name: Name of the operation to call
            **kwargs: Arguments to pass to the operation

        Returns:
            The response from the operation

        Raises:
            ISDSError: If there is an error calling the operation
        """
        try:
            operation = getattr(self.service, operation_name)
            response = operation(**kwargs)

            if self.debug:
                self.logger.debug(
                    f"Request to {operation_name}: {self.history.last_sent}"
                )
                self.logger.debug(
                    f"Response from {operation_name}: {self.history.last_received}"
                )

            if response is None:
                raise ISDSError(f"No response received from {operation_name}")

            return serialize_object(response)
        except exceptions.Fault as e:
            fault_detail = getattr(e, "detail", None)
            if fault_detail:
                if isinstance(fault_detail, bytes):
                    fault_detail = fault_detail.decode("utf-8")
                raise ISDSError(f"SOAP fault: {fault_detail}")
            raise ISDSError(f"SOAP fault: {str(e)}")
        except Exception as e:
            raise ISDSError(f"Error calling {operation_name}: {str(e)}")
