from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from schemas.status import DbStatus


class DataBoxType(str, Enum):
    """Data box type enumeration."""

    OVM = "OVM"  # Public authority
    PO = "PO"  # Legal entity
    PFO = "PFO"  # Individual - business
    FO = "FO"  # Individual


class DataBoxState(int, Enum):
    """Data box state enumeration."""

    INVALID = -1
    ALL = 0
    ACTIVE = 1
    INACTIVE = 2
    TERMINATED = 3


class OwnerInfo(BaseModel):
    """Data model for data box owner information."""

    db_id: Optional[str] = Field(None, alias="dbID")
    aifo_isds: Optional[bool] = Field(None, alias="aifoIsds")
    db_type: Optional[DataBoxType] = Field(None, alias="dbType")
    ic: Optional[str] = None
    pn_given_names: Optional[str] = Field(None, alias="pnGivenNames")
    pn_last_name: Optional[str] = Field(None, alias="pnLastName")
    firm_name: Optional[str] = Field(None, alias="firmName")
    bi_date: Optional[datetime] = Field(None, alias="biDate")
    bi_city: Optional[str] = Field(None, alias="biCity")
    bi_county: Optional[str] = Field(None, alias="biCounty")
    bi_state: Optional[str] = Field(None, alias="biState")
    ad_code: Optional[str] = Field(None, alias="adCode")
    ad_city: Optional[str] = Field(None, alias="adCity")
    ad_district: Optional[str] = Field(None, alias="adDistrict")
    ad_street: Optional[str] = Field(None, alias="adStreet")
    ad_number_in_street: Optional[str] = Field(None, alias="adNumberInStreet")
    ad_number_in_municipality: Optional[str] = Field(
        None, alias="adNumberInMunicipality"
    )
    ad_zip_code: Optional[str] = Field(None, alias="adZipCode")
    ad_state: Optional[str] = Field(None, alias="adState")
    nationality: Optional[str] = None
    db_id_ovm: Optional[str] = Field(None, alias="dbIdOVM")
    db_state: Optional[DataBoxState] = Field(None, alias="dbState")
    db_open_addressing: Optional[bool] = Field(None, alias="dbOpenAddressing")
    db_upper_id: Optional[str] = Field(None, alias="dbUpperID")

    class Config:
        use_enum_values = True
        populate_by_name = True


class DataBoxInfo(BaseModel):
    """Data model for data box information."""

    db_id: Optional[str] = Field(None, alias="dbID")
    db_type: Optional[DataBoxType] = Field(None, alias="dbType")
    ic: Optional[str] = None
    firm_name: Optional[str] = Field(None, alias="firmName")
    pn_given_names: Optional[str] = Field(None, alias="pnGivenNames")
    pn_last_name: Optional[str] = Field(None, alias="pnLastName")
    bi_date: Optional[datetime] = Field(None, alias="biDate")
    bi_city: Optional[str] = Field(None, alias="biCity")
    bi_county: Optional[str] = Field(None, alias="biCounty")
    bi_state: Optional[str] = Field(None, alias="biState")
    ad_code: Optional[str] = Field(None, alias="adCode")
    ad_city: Optional[str] = Field(None, alias="adCity")
    ad_district: Optional[str] = Field(None, alias="adDistrict")
    ad_street: Optional[str] = Field(None, alias="adStreet")
    ad_number_in_street: Optional[str] = Field(None, alias="adNumberInStreet")
    ad_number_in_municipality: Optional[str] = Field(
        None, alias="adNumberInMunicipality"
    )
    ad_zip_code: Optional[str] = Field(None, alias="adZipCode")
    ad_state: Optional[str] = Field(None, alias="adState")
    nationality: Optional[str] = None
    db_id_ovm: Optional[str] = Field(None, alias="dbIdOVM")
    db_state: Optional[DataBoxState] = Field(None, alias="dbState")
    db_effective_ovm: Optional[bool] = Field(None, alias="dbEffectiveOVM")
    db_open_addressing: Optional[bool] = Field(None, alias="dbOpenAddressing")

    class Config:
        use_enum_values = True
        populate_by_name = True


class FindDataBoxRequest(BaseModel):
    """Request model for finding data boxes."""

    owner_info: OwnerInfo = Field(..., alias="dbOwnerInfo")


class DbOwnerInfo(BaseModel):
    """Data model for data box owner information."""

    db_owner_info: DataBoxInfo = Field(..., alias="dbOwnerInfo")


class DbResults(BaseModel):
    """Data model for data box results."""

    list: List[DbOwnerInfo] = Field(..., alias="_value_1")


class FindDataBoxResponse(BaseModel):
    """Response model for finding data boxes."""

    results: DbResults = Field(..., alias="dbResults")
    status: DbStatus = Field(..., alias="dbStatus")


class CheckDataBoxResponse(BaseModel):
    """Response model for checking data box status."""

    db_info: DataBoxInfo = Field(..., alias="dbInfo")
    status: DbStatus = Field(..., alias="dbStatus")


class GetDataBoxListResponse(BaseModel):
    """Response model for getting data box list."""

    db_results: List[DataBoxInfo] = Field(..., alias="dbResults")
    status: DbStatus = Field(..., alias="dbStatus")


class PDZInfo(BaseModel):
    """Data model for PDZ information."""

    db_id: str = Field(..., alias="dbID")
    pdz_allowed: bool = Field(..., alias="pdzAllowed")
    pdz_effective_from: Optional[datetime] = Field(None, alias="pdzEffectiveFrom")
    pdz_effective_to: Optional[datetime] = Field(None, alias="pdzEffectiveTo")


class PDZInfoResponse(BaseModel):
    """Response model for PDZ information."""

    pdz_info: PDZInfo = Field(..., alias="pdzInfo")
    status: DbStatus = Field(..., alias="dbStatus")


class CreditInfo(BaseModel):
    """Data model for credit information."""

    db_id: str = Field(..., alias="dbID")
    credit_balance: int = Field(..., alias="creditBalance")
    credit_expiration: Optional[datetime] = Field(None, alias="creditExpiration")


class CreditInfoResponse(BaseModel):
    """Response model for credit information."""

    credit_info: CreditInfo = Field(..., alias="creditInfo")
    status: DbStatus = Field(..., alias="dbStatus")


# Import at the end to avoid circular imports
