from typing import Optional
from pydantic import BaseModel, Field


class DmStatus(BaseModel):
    """Data model for a dm status."""

    status_code: int = Field(..., alias="dmStatusCode")
    status_message: str = Field(..., alias="dmStatusMessage")


class DbStatus(BaseModel):
    """Data model for a data box status."""

    status_code: int = Field(..., alias="dbStatusCode")
    status_message: str = Field(..., alias="dbStatusMessage")
    status_ref_number: Optional[str] = Field(None, alias="dbStatusRefNumber")
