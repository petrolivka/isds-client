from pathlib import Path
from typing import Dict, Any
from .base import BaseService


class DataBoxAccessService(BaseService):
    """Service for data box access operations (db_access.wsdl)."""

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        wsdl_dir: Path,
    ):
        """Initialize the data box access service.

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
            wsdl_filename="db_access.wsdl",
            endpoint="DsManage",
        )

    def get_owner_info(self, login: str) -> Dict[str, Any]:
        """Get information about a data box owner by login.

        Args:
            login: Login username of the data box owner

        Returns:
            Owner information
        """
        return self._call("GetOwnerInfoFromLogin", dbOwnerLogin=login)

    def get_owner_info2(self, login: str) -> Dict[str, Any]:
        """Get extended information about a data box owner by login.

        Args:
            login: Login username of the data box owner

        Returns:
            Extended owner information
        """
        return self._call("GetOwnerInfoFromLogin2", dbOwnerLogin=login)

    def get_user_info2(self, login: str = "") -> Dict[str, Any]:
        """Get extended information about a data box user by login.

        Args:
            login: Login username of the data box user

        Returns:
            Extended user information
        """
        return self._call("GetUserInfoFromLogin2", dbDummy=login)

    def change_password(self, old_password: str, new_password: str) -> Dict[str, Any]:
        """Change ISDS password.

        Args:
            old_password: Current password
            new_password: New password

        Returns:
            Operation result
        """
        return self._call(
            "ChangeISDSPassword", dbOldPassword=old_password, dbNewPassword=new_password
        )

    def get_password_info(self, dummy: str = "") -> Dict[str, Any]:
        """Get information about the current password.

        Returns:
            Password information (e.g., expiration date)
        """
        return self._call("GetPasswordInfo", dbDummy=dummy)
