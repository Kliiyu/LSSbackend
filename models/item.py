from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class Item(BaseModel):
    name: str
    serial_number: str
    location_id: Optional[str]
    assigned_user: Optional[str]
    status: str = "available"
    warranty_expiration: Optional[datetime]
