from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List


class DmReceivedFile(BaseModel):
    dmMimeType: str = Field(..., description="Mime type")
    dmFileMetaType: str = Field(..., description="File meta type")
    dmFileDescr: str = Field(..., description="File description")
    dmFileGuid: Optional[str] = Field(None, description="File GUID")
    dmUpFileGuid: Optional[str] = Field(None, description="File GUID")
    dmFormat: Optional[str] = Field(None, description="File format")
    dmEncodedContent: Optional[bytes] = Field(None, description="Encoded content")
    dmXmlContent: Optional[str] = Field(None, description="XML content")


class DmFiles(BaseModel):
    dmFile: List[DmReceivedFile] = Field(..., description="Files")


class DmEnvelope(BaseModel):
    dmID: str = Field(..., description="Message ID")
    dbIDSender: str = Field(..., description="Sender's data box ID")
    dmSender: str = Field(..., description="Sender name")
    dmSenderAddress: Optional[str] = Field(None, description="Sender address")
    dmSenderType: int = Field(..., description="Sender type")
    dmRecipient: str = Field(..., description="Recipient name")
    dmRecipientAddress: Optional[str] = Field(None, description="Recipient address")
    dmAmbiguousRecipient: Optional[str] = Field(None, description="Ambiguous recipient")
    dmSenderOrgUnit: Optional[str] = Field(None, description="Sender organization unit")
    dmSenderOrgUnitNum: Optional[str] = Field(
        None, description="Sender organization unit number"
    )
    dbIDRecipient: str = Field(..., description="Recipient's data box ID")
    dmRecipientOrgUnit: Optional[str] = Field(
        None, description="Recipient organization unit"
    )
    dmRecipientOrgUnitNum: Optional[str] = Field(
        None, description="Recipient organization unit number"
    )
    dmToHands: Optional[str] = Field(None, description="To hands of")
    dmAnnotation: str = Field(..., description="Message annotation/subject")
    dmRecipientRefNumber: Optional[str] = Field(
        None, description="Recipient reference number"
    )
    dmSenderRefNumber: Optional[str] = Field(
        None, description="Sender reference number"
    )
    dmRecipientIdent: Optional[str] = Field(None, description="Recipient identifier")
    dmSenderIdent: Optional[str] = Field(None, description="Sender identifier")
    dmLegalTitleLaw: Optional[int] = Field(None, description="Legal title - law number")
    dmLegalTitleYear: Optional[int] = Field(None, description="Legal title - year")
    dmLegalTitleSect: Optional[str] = Field(None, description="Legal title - section")
    dmLegalTitlePar: Optional[str] = Field(None, description="Legal title - paragraph")
    dmLegalTitlePoint: Optional[str] = Field(None, description="Legal title - point")
    dmPersonalDelivery: bool = Field(..., description="Personal delivery required")
    dmAllowSubstDelivery: bool = Field(..., description="Allow substitute delivery")
    dmFiles: DmFiles = Field(..., description="Files")


class DmMessage(BaseModel):
    dmDm: DmEnvelope
    dmDeliveryTime: datetime = Field(..., description="Čas doručení")
    dmAcceptanceTime: datetime = Field(..., description="Čas akceptace")
    dmMessageStatus: int = Field(..., description="Status zprávy")
    dmAttachmentSize: int = Field(..., description="Velikost příloh")
    dmType: Optional[str] = Field(None, description="Typ zprávy")
