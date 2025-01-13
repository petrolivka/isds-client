from pathlib import Path
from typing import Dict, Any, List
from .base import BaseService


class MessageOperationsService(BaseService):
    """Service for message operations (dm_operations.wsdl)."""

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        wsdl_dir: Path,
    ):
        """Initialize the message operations service.

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
            wsdl_filename="dm_operations.wsdl",
            endpoint="dz",
        )

    def create_message(
        self, recipient_id: str, subject: str, content: str, **kwargs
    ) -> Dict[str, Any]:
        """Create and send a new message.

        Args:
            recipient_id: ID of the recipient's data box
            subject: Subject of the message
            content: Content of the message
            **kwargs: Additional message parameters

        Returns:
            Response containing the created message details
        """
        params = {
            "dmEnvelope": {
                "dbIDRecipient": recipient_id,
                "dmAnnotation": subject,
            },
            "dmContent": content,
            **kwargs,
        }
        return self._call("CreateMessage", **params)

    def create_multiple_message(
        self, recipient_ids: List[str], subject: str, content: str, **kwargs
    ) -> Dict[str, Any]:
        """Create and send a message to multiple recipients.

        Args:
            recipient_ids: List of recipient data box IDs
            subject: Subject of the message
            content: Content of the message
            **kwargs: Additional message parameters

        Returns:
            Response containing the created message details
        """
        params = {
            "dmEnvelope": {
                "dbIDRecipient": recipient_ids,
                "dmAnnotation": subject,
            },
            "dmContent": content,
            **kwargs,
        }
        return self._call("CreateMultipleMessage", **params)

    def download_message(self, message_id: str) -> Dict[str, Any]:
        """Download a received message.

        Args:
            message_id: ID of the message to download

        Returns:
            The complete message content
        """
        return self._call("MessageDownload", dmID=message_id)

    def download_signed_message(self, message_id: str) -> Dict[str, Any]:
        """Download a signed received message.

        Args:
            message_id: ID of the message to download

        Returns:
            The complete signed message content
        """
        return self._call("SignedMessageDownload", dmID=message_id)

    def download_signed_sent_message(self, message_id: str) -> Dict[str, Any]:
        """Download a signed sent message.

        Args:
            message_id: ID of the message to download

        Returns:
            The complete signed message content
        """
        return self._call("SignedSentMessageDownload", dmID=message_id)

    def authenticate_message(self, message_id: str) -> Dict[str, Any]:
        """Verify the authenticity of a message.

        Args:
            message_id: ID of the message to verify

        Returns:
            Authentication result
        """
        return self._call("AuthenticateMessage", dmID=message_id)

    def resign_document(self, message_id: str) -> Dict[str, Any]:
        """Re-sign an ISDS document.

        Args:
            message_id: ID of the document to re-sign

        Returns:
            Result of the re-signing operation
        """
        return self._call("Re-signISDSDocument", dmID=message_id)
