"""Data box info service implementation."""

from typing import Any
from .base import BaseService


class DataBoxInfoService(BaseService):
    """Service for data box info operations."""

    @property
    def wsdl_filename(self) -> str:
        return "dm_info.wsdl"

    def get_databox_activity_status(self, **kwargs) -> Any:
        """Get activity status of a data box."""
        return self._call("GetDataBoxActivityStatus", **kwargs)

    def get_received_messages(self, **kwargs) -> Any:
        """Get list of received messages based on filter parameters.

        Args:
            params: Filter parameters including date range, offset and limit
        """
        if not kwargs.get("from_date") and not kwargs.get("to_date"):
            # If no dates provided, use defaults
            from datetime import datetime, timedelta

            kwargs["from_date"] = datetime.now() - timedelta(days=90)  # Last 90 days
            kwargs["to_date"] = datetime.now()

        if not kwargs.get("limit"):
            kwargs["limit"] = 1000  # Default limit

        if not kwargs.get("offset"):
            kwargs["offset"] = 1  # Default offset (1-based)

        return self._call("GetListOfReceivedMessages", **kwargs)

    def get_sent_messages(self, **kwargs) -> Any:
        """Get list of sent messages based on filter parameters."""
        return self._call("GetListOfSentMessages", **kwargs)
