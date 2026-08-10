from enum import Enum
from datetime import datetime

from pydantic import BaseModel,EmailStr,Field

## creating class for the property type
class PropertyType(str,Enum):
    APPARTMENT="apartment"
    VILLA="villa"
    PLOT = "plot"
    COMMERCIAL = "commercial"

## creating class for lead soource
class LeadSource(str,Enum):
    WEBSITE = "website"
    WHATSAPP = "whatsapp"
    PHONE = "phone"
    REFERRAL = "referral"
    WALK_IN = "walk_in"

## creating class for lead status

class LeadStatus(str, Enum):
    NEW = "new"
    CONTACTED = "contacted"
    INTERESTED = "interested"
    SITE_VISIT = "site_visit"
    NEGOTIATION = "negotiation"
    CLOSED = "closed"
    LOST = "lost"



## creating class for create lead
class LeadCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr | None = None
    property_type: PropertyType
    source: LeadSource
    budget: float | None = None


# creating class for updating the class
class LeadUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    property_type: PropertyType | None = None
    source: LeadSource | None = None
    status: LeadStatus | None = None
    budget: float | None = None


# creatting class for lead response
class LeadResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: EmailStr | None = None
    property_type: PropertyType
    source: LeadSource
    status: LeadStatus

    




