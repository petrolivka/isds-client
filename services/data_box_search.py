from pathlib import Path
from typing import Dict, Any
from .base import BaseService


class DataBoxSearchService(BaseService):
    """Service for data box search operations (db_search.wsdl)."""

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        wsdl_dir: Path,
        debug: bool = False,
    ):
        """Initialize the data box search service.

        Args:
            username: Login username
            password: Password
            base_url: Base URL of the ISDS service
            wsdl_dir: Directory containing WSDL files
            debug: If True, enable debug logging
        """
        super().__init__(
            username=username,
            password=password,
            base_url=base_url,
            wsdl_dir=wsdl_dir,
            wsdl_filename="db_search.wsdl",
            endpoint="df",
            debug=debug,
        )

    def find_data_box2(self, **kwargs) -> Any:
        """Find a data box with extended search parameters.

        Args:
            **kwargs: Search parameters (e.g., dbOwnerInfo, dbState, etc.)

        Returns:
            List of found data boxes
        """
        response = self._call("FindDataBox2", **kwargs)
        return response

    def check_data_box(self, data_box_id: str) -> Any:
        """Check if a data box exists and get its status.

        Args:
            data_box_id: ID of the data box to check

        Returns:
            Data box status information
        """
        return self._call("CheckDataBox", dbID=data_box_id)

    def isds_search_3(self, search_text: str, **kwargs) -> Any:
        """Get a list of data boxes based on criteria.

        Args:
            **kwargs: Filter parameters

        Returns:
            List of data boxes
        """
        return self._call("ISDSSearch3", searchText=search_text, **kwargs)

    def get_credit_info(self, data_box_id: str) -> Any:
        """Get credit information for a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            Credit information
        """
        return self._call("DataBoxCreditInfo", dbID=data_box_id)

    def get_activity_status(self, data_box_id: str) -> Dict[str, Any]:
        """Get activity status of a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            Activity status information
        """
        return self._call("GetDataBoxActivityStatus", dbID=data_box_id)
