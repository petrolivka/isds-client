from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime
from .base import BaseService


class DataBoxSearchService(BaseService):
    """Service for data box search operations (db_search.wsdl)."""

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        wsdl_dir: Path,
    ):
        """Initialize the data box search service.

        Args:
            username: Login username
            password: Password
            base_url: Base URL of the ISDS service
            wsdl_dir: Directory containing WSDL files
        """
        super().__init__(
            username=username,
            password=password,
            base_url=base_url,
            wsdl_dir=wsdl_dir,
            wsdl_filename="db_search.wsdl",
            endpoint="df",
        )

    def find_data_box(self, search_text: str, **kwargs) -> Dict[str, Any]:
        """Find a data box by search text.

        Args:
            search_text: Text to search for
            **kwargs: Additional search parameters

        Returns:
            List of found data boxes
        """
        return self._call("FindDataBox", searchText=search_text, **kwargs)

    def find_data_box2(self, **kwargs) -> Dict[str, Any]:
        """Find a data box with extended search parameters.

        Args:
            **kwargs: Search parameters (e.g., dbOwnerInfo, dbState, etc.)

        Returns:
            List of found data boxes
        """
        return self._call("FindDataBox2", **kwargs)

    def check_data_box(self, data_box_id: str) -> Dict[str, Any]:
        """Check if a data box exists and get its status.

        Args:
            data_box_id: ID of the data box to check

        Returns:
            Data box status information
        """
        return self._call("CheckDataBox", dbID=data_box_id)

    def get_data_box_list(self, **kwargs) -> Dict[str, Any]:
        """Get a list of data boxes based on criteria.

        Args:
            **kwargs: Filter parameters

        Returns:
            List of data boxes
        """
        return self._call("GetDataBoxList", **kwargs)

    def get_pdz_info(self, data_box_id: str) -> Dict[str, Any]:
        """Get PDZ (Postal Data Message) information for a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            PDZ information
        """
        return self._call("PDZInfo", dbID=data_box_id)

    def get_credit_info(self, data_box_id: str) -> Dict[str, Any]:
        """Get credit information for a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            Credit information
        """
        return self._call("DataBoxCreditInfo", dbID=data_box_id)

    def search_isds2(self, **kwargs) -> Dict[str, Any]:
        """Search ISDS with extended parameters (version 2).

        Args:
            **kwargs: Search parameters

        Returns:
            Search results
        """
        return self._call("ISDSSearch2", **kwargs)

    def search_isds3(self, **kwargs) -> Dict[str, Any]:
        """Search ISDS with extended parameters (version 3).

        Args:
            **kwargs: Search parameters

        Returns:
            Search results
        """
        return self._call("ISDSSearch3", **kwargs)

    def get_activity_status(self, data_box_id: str) -> Dict[str, Any]:
        """Get activity status of a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            Activity status information
        """
        return self._call("GetDataBoxActivityStatus", dbID=data_box_id)

    def find_personal_data_box(self, **kwargs) -> Dict[str, Any]:
        """Find a personal data box.

        Args:
            **kwargs: Search parameters (e.g., birth_date, surname, etc.)

        Returns:
            Found personal data box information
        """
        return self._call("FindPersonalDataBox", **kwargs)

    def get_dt_info(self, data_box_id: str) -> Dict[str, Any]:
        """Get DT (Trusted Data) information for a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            DT information
        """
        return self._call("DTInfo", dbID=data_box_id)

    def get_pdz_send_info(self, data_box_id: str) -> Dict[str, Any]:
        """Get PDZ sending information for a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            PDZ sending information
        """
        return self._call("PDZSendInfo", dbID=data_box_id)

    def get_constants(self) -> Dict[str, Any]:
        """Get system constants.

        Returns:
            System constants
        """
        return self._call("GetConstants")

    def get_data_box_address(self, data_box_id: str) -> Dict[str, Any]:
        """Get address information for a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            Data box address information
        """
        return self._call("GetDataBoxAddress", dbID=data_box_id)
