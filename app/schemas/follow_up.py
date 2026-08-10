from datetime import datetime
from pydantic import BaseModel

class FollowUpCreate(BaseModel):
    content:str
    next_follow_up_date: datetime |None=None

class FollowUpResponse(BaseModel):
    id: int
    lead_id: int
    content: str
    next_follow_up_date: datetime | None = None
    created_at: datetime
    