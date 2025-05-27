from pydantic import BaseModel
from typing import Optional

class Stored(BaseModel):
    name: str
    category: str
    location_id: Optional[str]
    stock: int
