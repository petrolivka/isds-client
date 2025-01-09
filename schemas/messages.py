from datetime import datetime
from enum import IntEnum
from typing import List, Optional
from pydantic import BaseModel, Field


class MessageStatus(IntEnum):
    """Message status enumeration."""

    CREATED = 1
    DELIVERED = 2
    DELIVERED_BY_FICTION = 3
    DELIVERED_BY_LOGIN = 4
    UNDELIVERABLE = 5
    ACCEPTED = 6
    READ = 7
    CANCELLED = 8
    DELETED = 9


class SenderType(IntEnum):
    """Sender type enumeration."""

    SYSTEM = 0
    OVM = 10
    PO = 20
    PFO = 30
    FO = 40


class DmStatus(BaseModel):
    """Data model for a dm status."""

    status_code: int = Field(..., alias="dmStatusCode")
    status_message: str = Field(..., alias="dmStatusMessage")


class DmRecords(BaseModel):
    """Data model for a dm records."""

    records: List["MessageRecordEnvelope"] = Field(..., alias="_value_1")


class GetReceivedMessagesResponse(BaseModel):
    """Data model for a message record."""

    records: DmRecords = Field(..., alias="dmRecords")
    status: DmStatus = Field(..., alias="dmStatus")


class MessageRecordEnvelope(BaseModel):
    """Data model for a message record envelope."""

    record: "MessageRecord" = Field(..., alias="dmRecord")


class MessageRecord(BaseModel):
    """Data model for a message record."""

    ordinal: int = Field(..., alias="dmOrdinal")
    id: str = Field(..., alias="dmID")
    sender_id: str = Field(..., alias="dbIDSender")
    sender: str = Field(..., alias="dmSender")
    sender_address: Optional[str] = Field(None, alias="dmSenderAddress")
    sender_type: SenderType = Field(..., alias="dmSenderType")
    recipient: str = Field(..., alias="dmRecipient")
    recipient_address: Optional[str] = Field(None, alias="dmRecipientAddress")
    ambiguous_recipient: Optional[str] = Field(None, alias="dmAmbiguousRecipient")
    sender_org_unit: Optional[str] = Field(None, alias="dmSenderOrgUnit")
    sender_org_unit_num: Optional[str] = Field(None, alias="dmSenderOrgUnitNum")
    recipient_id: str = Field(..., alias="dbIDRecipient")
    recipient_org_unit: Optional[str] = Field(None, alias="dmRecipientOrgUnit")
    recipient_org_unit_num: Optional[str] = Field(None, alias="dmRecipientOrgUnitNum")
    to_hands: Optional[str] = Field(None, alias="dmToHands")
    subject: str = Field(..., alias="dmAnnotation")
    recipient_ref_number: Optional[str] = Field(None, alias="dmRecipientRefNumber")
    sender_ref_number: Optional[str] = Field(None, alias="dmSenderRefNumber")
    recipient_ident: Optional[str] = Field(None, alias="dmRecipientIdent")
    sender_ident: Optional[str] = Field(None, alias="dmSenderIdent")
    legal_title_law: Optional[int] = Field(None, alias="dmLegalTitleLaw")
    legal_title_year: Optional[int] = Field(None, alias="dmLegalTitleYear")
    legal_title_sect: Optional[str] = Field(None, alias="dmLegalTitleSect")
    legal_title_par: Optional[str] = Field(None, alias="dmLegalTitlePar")
    legal_title_point: Optional[str] = Field(None, alias="dmLegalTitlePoint")
    personal_delivery: bool = Field(False, alias="dmPersonalDelivery")
    allow_subst_delivery: bool = Field(False, alias="dmAllowSubstDelivery")
    status: MessageStatus = Field(..., alias="dmMessageStatus")
    attachment_size: int = Field(..., alias="dmAttachmentSize")
    delivery_time: Optional[datetime] = Field(None, alias="dmDeliveryTime")
    acceptance_time: Optional[datetime] = Field(None, alias="dmAcceptanceTime")
    type: Optional[str] = Field(None, alias="dmType")
    vodz: Optional[str] = Field(None, alias="dmVODZ")

    class Config:
        """Pydantic model configuration."""

        use_enum_values = True
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}
