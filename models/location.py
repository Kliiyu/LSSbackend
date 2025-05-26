from pydantic import BaseModel
from typing import Optional, List

class Location(BaseModel):
    location_name: str
    room: Optional[str]
    items: Optional[List[str]] = []
