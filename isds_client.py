from pathlib import Path
from typing import List, Optional, Dict, Any
from datetime import datetime

from schemas.base import DmFile
from services import (
    MessageOperationsService,
    MessageInfoService,
    DataBoxSearchService,
    DataBoxAccessService,
)


class ISDSClient:
    """Client for Czech Data Box Information System (ISDS)."""

    def __init__(
        self,
        username: str,
        password: str,
        production: bool = False,
        wsdl_dir: Optional[Path] = None,
        debug: bool = False,
    ):
        """Initialize ISDS client.

        Args:
            username: Login username
            password: Login password
            production: If True, use production environment, otherwise test
            wsdl_dir: Directory containing WSDL files (defaults to ./wsdl)
            debug: If True, enable debug logging
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
        self._message_operations = MessageOperationsService(
            username=username,
            password=password,
            base_url=self.base_url,
            wsdl_dir=self.wsdl_dir,
            debug=debug,
        )
        self._message_info = MessageInfoService(
            username=username,
            password=password,
            base_url=self.base_url,
            wsdl_dir=self.wsdl_dir,
            debug=debug,
        )
        self._data_box_search = DataBoxSearchService(
            username=username,
            password=password,
            base_url=self.base_url,
            wsdl_dir=self.wsdl_dir,
            debug=debug,
        )
        self._data_box_access = DataBoxAccessService(
            username=username,
            password=password,
            base_url=self.base_url,
            wsdl_dir=self.wsdl_dir,
            debug=debug,
        )

    # Message Operations methods
    def create_message(
        self, recipient_id: str, subject: str, files: List[DmFile], **kwargs
    ) -> Dict[str, Any]:
        """Create and send a new message."""
        return self._message_operations.create_message(
            recipient_id=recipient_id, subject=subject, files=files, **kwargs
        )

    def download_message(self, message_id: str) -> Dict[str, Any]:
        """Download a message."""
        return self._message_operations.download_message(message_id)

    def download_signed_message(self, message_id: str) -> Dict[str, Any]:
        """Download a signed message."""
        return self._message_operations.download_signed_message(message_id)

    def authenticate_message(self, message_id: str) -> Dict[str, Any]:
        """Verify the authenticity of a message."""
        return self._message_operations.authenticate_message(message_id)

    # Message Info methods
    def get_message_info(self, message_id: str) -> Dict[str, Any]:
        """Get state changes for a message."""
        return self._message_info.get_message_state_changes(message_id)

    def get_delivery_info(self, message_id: str) -> Dict[str, Any]:
        """Get delivery information for a message."""
        return self._message_info.get_delivery_info(message_id)

    def get_sent_messages(
        self,
        from_time: Optional[datetime] = None,
        to_time: Optional[datetime] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Get list of sent messages."""
        return self._message_info.get_sent_messages(
            from_time=from_time,
            to_time=to_time,
            **kwargs,
        )

    def get_received_messages(
        self,
        from_time: Optional[datetime] = None,
        to_time: Optional[datetime] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Get list of received messages."""
        return self._message_info.get_received_messages(
            from_time=from_time,
            to_time=to_time,
            **kwargs,
        )

    def mark_message_as_downloaded(self, message_id: str) -> Dict[str, Any]:
        """Mark a message as downloaded/read."""
        return self._message_info.mark_message_as_downloaded(message_id)

    def get_message_envelope(self, message_id: str) -> Dict[str, Any]:
        """Get the envelope of a message."""
        return self._message_info.get_message_envelope(message_id)

    def get_list_of_erased_messages(self, **kwargs) -> Dict[str, Any]:
        """Get list of erased messages."""
        return self._message_info.get_erased_messages(**kwargs)

    def register_for_notifications(self, **kwargs) -> Dict[str, Any]:
        """Register for external notifications."""
        return self._message_info.register_for_notifications(**kwargs)

    def get_notification_list(self, **kwargs) -> Dict[str, Any]:
        """Get list of notifications."""
        return self._message_info.get_notification_list(**kwargs)

    def get_sent_message_envelope(self, message_id: str) -> Dict[str, Any]:
        """Get the envelope of a sent message."""
        return self._message_info.get_sent_message_envelope(message_id)

    def verify_message(self, message_id: str) -> Dict[str, Any]:
        """Verify the authenticity of a message."""
        return self._message_info.verify_message(message_id)

    # Data Box Search methods
    def find_data_box(self, owner_info: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Find a data box by search parameters."""
        return self._data_box_search.find_data_box2(dbOwnerInfo=owner_info, **kwargs)

    def check_data_box(self, data_box_id: str) -> Dict[str, Any]:
        """Check if a data box exists and get its status."""
        return self._data_box_search.check_data_box(data_box_id)

    def get_data_box_list(self, **kwargs) -> Dict[str, Any]:
        """Get a list of data boxes based on criteria."""
        return self._data_box_search.get_data_box_list(**kwargs)

    def get_credit_info(self, data_box_id: str) -> Dict[str, Any]:
        """Get credit information for a data box."""
        return self._data_box_search.get_credit_info(data_box_id)

    # Data Box Access methods
    def get_owner_info(self) -> Dict[str, Any]:
        """Get information about a data box owner."""
        return self._data_box_access.get_owner_info2()

    def get_user_info(self) -> Dict[str, Any]:
        """Get information about a data box user."""
        return self._data_box_access.get_user_info2()

    def change_password(self, old_password: str, new_password: str) -> Dict[str, Any]:
        """Change ISDS password."""
        return self._data_box_access.change_password(old_password, new_password)

    def get_password_info(self) -> Dict[str, Any]:
        """Get information about the current password."""
        return self._data_box_access.get_password_info()
