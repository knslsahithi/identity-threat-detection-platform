from pydantic import BaseModel


class IdentityEvent(BaseModel):
    timestamp: str
    user: str
    location: str
    device: str
    application: str
    status: str