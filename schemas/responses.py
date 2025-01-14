from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any

from schemas.message import DmEnvelope, DmMessage


class DmStatus(BaseModel):
    dmStatusCode: str = Field(..., description="Status kód")
    dmStatusMessage: str = Field(..., description="Status zpráva")


class DownloadMessageResponse(BaseModel):
    dmReturnedMessage: DmMessage
    dmStatus: DmStatus
