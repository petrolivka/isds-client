from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

from schemas.messages import (
    GetReceivedMessagesResponse,
    MessageStatus,
    VerifyMessageResponse,
)
from .base import BaseService


class MessageInfoService(BaseService):
    """Service for message info operations (dm_info.wsdl)."""

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        wsdl_dir: Path,
    ):
        """Initialize the message info service.

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
            wsdl_filename="dm_info.wsdl",
            endpoint="dx",
        )

    def verify_message(self, message_id: str) -> VerifyMessageResponse:
        """Verify the integrity of a message.

        Args:
            message_id: ID of the message to verify

        Returns:
            Verification result
        """
        return VerifyMessageResponse.model_validate(
            self._call("VerifyMessage", dmID=message_id)
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
        status_filter: Optional[MessageStatus] = MessageStatus.ALL,
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
            "dmStatusFilter": status_filter.value if status_filter else -1,
            **kwargs,
        }
        return self._call("GetListOfSentMessages", **params)

    def get_received_messages(
        self,
        from_time: Optional[datetime] = None,
        to_time: Optional[datetime] = None,
        status_filter: Optional[MessageStatus] = MessageStatus.ALL,
        **kwargs,
    ) -> GetReceivedMessagesResponse:
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
            "dmStatusFilter": status_filter.value if status_filter else -1,
            **kwargs,
        }
        return GetReceivedMessagesResponse.model_validate(
            self._call("GetListOfReceivedMessages", **params)
        )

    def get_message_state_changes(self, message_id: str) -> Dict[str, Any]:
        """Get state changes for a message.

        Args:
            message_id: ID of the message

        Returns:
            List of message state changes
        """
        return self._call("GetMessageStateChanges", dmID=message_id)

    def get_message_author(self, message_id: str) -> Dict[str, Any]:
        """Get information about the message sender.

        Args:
            message_id: ID of the message

        Returns:
            Information about the message sender
        """
        return self._call("GetMessageAuthor", dmID=message_id)

    def get_message_author2(self, message_id: str) -> Dict[str, Any]:
        """Get extended information about the message sender.

        Args:
            message_id: ID of the message

        Returns:
            Extended information about the message sender
        """
        return self._call("GetMessageAuthor2", dmID=message_id)

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
