from pydantic import BaseModel


class LeaveCreate(BaseModel):
    reason: str
    from_date: str
    to_date: str


class LeaveApprove(BaseModel):
    status: str