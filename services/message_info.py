from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

from .base import BaseService


class MessageInfoService(BaseService):
    """Service for message info operations (dm_info.wsdl)."""

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        wsdl_dir: Path,
        debug: bool = False,
    ):
        """Initialize the message info service.

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
            wsdl_filename="dm_info.wsdl",
            endpoint="dx",
            debug=debug,
        )

    def get_message_envelope(self, message_id: str) -> Dict[str, Any]:
        """Get the envelope of a received message.

        Args:
            message_id: ID of the message

        Returns:
            Message envelope in readable form
        """
        return self._call("MessageEnvelopeDownload", dmID=message_id)

    def mark_message_as_downloaded(self, message_id: str) -> Dict[str, Any]:
        """Mark a received message as downloaded/read.

        Args:
            message_id: ID of the message

        Returns:
            Operation result
        """
        return self._call("MarkMessageAsDownloaded", dmID=message_id)

    def get_delivery_info(self, message_id: str) -> Dict[str, Any]:
        """Get delivery information for a message.

        Args:
            message_id: ID of the message

        Returns:
            Delivery information (delivery receipt, acceptance receipt, or non-delivery notice)
        """
        return self._call("GetDeliveryInfo", dmID=message_id)

    def get_signed_delivery_info(self, message_id: str) -> Dict[str, Any]:
        """Get signed delivery information for a message.

        Args:
            message_id: ID of the message

        Returns:
            Signed delivery information
        """
        return self._call("GetSignedDeliveryInfo", dmID=message_id)

    def get_sent_messages(
        self,
        from_time: Optional[datetime] = None,
        to_time: Optional[datetime] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Get list of sent messages.

        Args:
            from_time: Start time for the list
            to_time: End time for the list
            **kwargs: Additional filter parameters

        Returns:
            List of sent messages
        """
        params = {
            **({"dmFromTime": from_time} if from_time else {}),
            **({"dmToTime": to_time} if to_time else {}),
            **(
                {"dmStatusFilter": kwargs.get("status_filter")}
                if kwargs.get("status_filter")
                else {"dmStatusFilter": -1}
            ),
            **kwargs,
        }
        return self._call("GetListOfSentMessages", **params)

    def get_received_messages(
        self,
        from_time: Optional[datetime] = None,
        to_time: Optional[datetime] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Get list of received messages.

        Args:
            from_time: Start time for the list
            to_time: End time for the list
            **kwargs: Additional filter parameters

        Returns:
            List of received messages
        """
        params = {
            **({"dmFromTime": from_time} if from_time else {}),
            **({"dmToTime": to_time} if to_time else {}),
            **(
                {"dmStatusFilter": kwargs.get("status_filter")}
                if kwargs.get("status_filter")
                else {"dmStatusFilter": -1}
            ),
            **kwargs,
        }
        return self._call("GetListOfReceivedMessages", **params)

    def get_message_state_changes(
        self, dmFromTime: datetime, dmToTime: datetime
    ) -> Dict[str, Any]:
        """Get state changes for a message.

        Args:
            message_id: ID of the message

        Returns:
            List of message state changes
        """
        return self._call(
            "GetMessageStateChanges", dmFromTime=dmFromTime, dmToTime=dmToTime
        )

    def erase_message(self, message_id: str) -> Dict[str, Any]:
        """Erase a long-term stored message.

        Args:
            message_id: ID of the message to erase

        Returns:
            Operation result
        """
        return self._call("EraseMessage", dmID=message_id)

    def get_erased_messages(
        self,
        from_time: Optional[datetime] = None,
        to_time: Optional[datetime] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Get list of erased messages.

        Args:
            from_time: Start time for the list
            to_time: End time for the list
            **kwargs: Additional filter parameters

        Returns:
            List of erased messages
        """
        params = {
            **({"dmFromTime": from_time} if from_time else {}),
            **({"dmToTime": to_time} if to_time else {}),
            **kwargs,
        }
        return self._call("GetListOfErasedMessages", **params)

    def register_for_notifications(self, **kwargs) -> Dict[str, Any]:
        """Register for external notifications.

        Args:
            **kwargs: Notification parameters

        Returns:
            Registration result
        """
        return self._call("RegisterForNotifications", **kwargs)

    def get_notification_list(self, **kwargs) -> Dict[str, Any]:
        """Get list of notifications.

        Args:
            **kwargs: Filter parameters

        Returns:
            List of notifications
        """
        return self._call("GetListForNotifications", **kwargs)

    def get_sent_message_envelope(self, message_id: str) -> Dict[str, Any]:
        """Get the envelope of a sent message.

        Args:
            message_id: ID of the message

        Returns:
            Message envelope
        """
        return self._call("SentMessageEnvelopeDownload", dmID=message_id)

    def verify_message(self, message_id: str) -> Dict[str, Any]:
        """Verify the authenticity of a message."""
        return self._call("VerifyMessage", dmID=message_id)
