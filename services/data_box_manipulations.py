from pathlib import Path
from typing import Optional, Dict, Any, List
from .base import BaseService


class DataBoxManipulationsService(BaseService):
    """Service for data box manipulation operations (db_manipulations.wsdl)."""

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        wsdl_dir: Path,
    ):
        """Initialize the data box manipulations service.

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
            wsdl_filename="db_manipulations.wsdl",
            endpoint="dbm",
        )

    def create_data_box(self, **kwargs) -> Dict[str, Any]:
        """Create a new data box.

        Args:
            **kwargs: Data box creation parameters (e.g., owner info, type, etc.)

        Returns:
            Created data box information
        """
        return self._call("CreateDataBox", **kwargs)

    def create_data_box2(self, **kwargs) -> Dict[str, Any]:
        """Create a new data box with extended parameters.

        Args:
            **kwargs: Extended data box creation parameters

        Returns:
            Created data box information
        """
        return self._call("CreateDataBox2", **kwargs)

    def delete_data_box(self, data_box_id: str) -> Dict[str, Any]:
        """Delete a data box.

        Args:
            data_box_id: ID of the data box to delete

        Returns:
            Operation result
        """
        return self._call("DeleteDataBox", dbID=data_box_id)

    def delete_data_box2(self, data_box_id: str, **kwargs) -> Dict[str, Any]:
        """Delete a data box with extended parameters.

        Args:
            data_box_id: ID of the data box to delete
            **kwargs: Additional deletion parameters

        Returns:
            Operation result
        """
        return self._call("DeleteDataBox2", dbID=data_box_id, **kwargs)

    def update_data_box_description(self, data_box_id: str, **kwargs) -> Dict[str, Any]:
        """Update data box description.

        Args:
            data_box_id: ID of the data box to update
            **kwargs: Description update parameters

        Returns:
            Operation result
        """
        return self._call("UpdateDataBoxDescr", dbID=data_box_id, **kwargs)

    def update_data_box_description2(
        self, data_box_id: str, **kwargs
    ) -> Dict[str, Any]:
        """Update data box description with extended parameters.

        Args:
            data_box_id: ID of the data box to update
            **kwargs: Extended description update parameters

        Returns:
            Operation result
        """
        return self._call("UpdateDataBoxDescr2", dbID=data_box_id, **kwargs)

    def add_data_box_user(self, data_box_id: str, **kwargs) -> Dict[str, Any]:
        """Add a user to a data box.

        Args:
            data_box_id: ID of the data box
            **kwargs: User information parameters

        Returns:
            Operation result
        """
        return self._call("AddDataBoxUser", dbID=data_box_id, **kwargs)

    def add_data_box_user2(self, data_box_id: str, **kwargs) -> Dict[str, Any]:
        """Add a user to a data box with extended parameters.

        Args:
            data_box_id: ID of the data box
            **kwargs: Extended user information parameters

        Returns:
            Operation result
        """
        return self._call("AddDataBoxUser2", dbID=data_box_id, **kwargs)

    def delete_data_box_user(self, user_id: str) -> Dict[str, Any]:
        """Delete a user from a data box.

        Args:
            user_id: ID of the user to delete

        Returns:
            Operation result
        """
        return self._call("DeleteDataBoxUser", dbUserID=user_id)

    def delete_data_box_user2(self, user_id: str, **kwargs) -> Dict[str, Any]:
        """Delete a user from a data box with extended parameters.

        Args:
            user_id: ID of the user to delete
            **kwargs: Additional deletion parameters

        Returns:
            Operation result
        """
        return self._call("DeleteDataBoxUser2", dbUserID=user_id, **kwargs)

    def update_data_box_user(self, user_id: str, **kwargs) -> Dict[str, Any]:
        """Update data box user information.

        Args:
            user_id: ID of the user to update
            **kwargs: User information update parameters

        Returns:
            Operation result
        """
        return self._call("UpdateDataBoxUser", dbUserID=user_id, **kwargs)

    def update_data_box_user2(self, user_id: str, **kwargs) -> Dict[str, Any]:
        """Update data box user information with extended parameters.

        Args:
            user_id: ID of the user to update
            **kwargs: Extended user information update parameters

        Returns:
            Operation result
        """
        return self._call("UpdateDataBoxUser2", dbUserID=user_id, **kwargs)

    def new_access_data(self, user_id: str) -> Dict[str, Any]:
        """Generate new access data for a user.

        Args:
            user_id: ID of the user

        Returns:
            New access data
        """
        return self._call("NewAccessData", dbUserID=user_id)

    def new_access_data2(self, user_id: str, **kwargs) -> Dict[str, Any]:
        """Generate new access data for a user with extended parameters.

        Args:
            user_id: ID of the user
            **kwargs: Additional parameters

        Returns:
            New access data
        """
        return self._call("NewAccessData2", dbUserID=user_id, **kwargs)

    def disable_data_box_externally(self, data_box_id: str, **kwargs) -> Dict[str, Any]:
        """Disable a data box externally.

        Args:
            data_box_id: ID of the data box to disable
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        return self._call("DisableDataBoxExternally", dbID=data_box_id, **kwargs)

    def disable_data_box_externally2(
        self, data_box_id: str, **kwargs
    ) -> Dict[str, Any]:
        """Disable a data box externally with extended parameters.

        Args:
            data_box_id: ID of the data box to disable
            **kwargs: Extended parameters

        Returns:
            Operation result
        """
        return self._call("DisableDataBoxExternally2", dbID=data_box_id, **kwargs)

    def disable_own_data_box(self, **kwargs) -> Dict[str, Any]:
        """Disable own data box.

        Args:
            **kwargs: Disable parameters

        Returns:
            Operation result
        """
        return self._call("DisableOwnDataBox", **kwargs)

    def disable_own_data_box2(self, **kwargs) -> Dict[str, Any]:
        """Disable own data box with extended parameters.

        Args:
            **kwargs: Extended disable parameters

        Returns:
            Operation result
        """
        return self._call("DisableOwnDataBox2", **kwargs)

    def enable_own_data_box(self, **kwargs) -> Dict[str, Any]:
        """Enable own data box.

        Args:
            **kwargs: Enable parameters

        Returns:
            Operation result
        """
        return self._call("EnableOwnDataBox", **kwargs)

    def enable_own_data_box2(self, **kwargs) -> Dict[str, Any]:
        """Enable own data box with extended parameters.

        Args:
            **kwargs: Extended enable parameters

        Returns:
            Operation result
        """
        return self._call("EnableOwnDataBox2", **kwargs)

    def set_open_addressing(self, data_box_id: str) -> Dict[str, Any]:
        """Enable open addressing for a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            Operation result
        """
        return self._call("SetOpenAddressing", dbID=data_box_id)

    def clear_open_addressing(self, data_box_id: str) -> Dict[str, Any]:
        """Disable open addressing for a data box.

        Args:
            data_box_id: ID of the data box

        Returns:
            Operation result
        """
        return self._call("ClearOpenAddressing", dbID=data_box_id)

    def get_data_box_users2(self, data_box_id: str) -> Dict[str, Any]:
        """Get list of users for a data box (version 2).

        Args:
            data_box_id: ID of the data box

        Returns:
            List of data box users
        """
        return self._call("GetDataBoxUsers2", dbID=data_box_id)
