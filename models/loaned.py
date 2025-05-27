from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Loaned(BaseModel):
    name: str
    serial_number: str
    category: str
    location_id: Optional[str]
    assigned_user: Optional[str]
    status: str = "available"
    loan_expiration: Optional[datetime]
