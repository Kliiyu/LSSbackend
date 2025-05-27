from pydantic import BaseModel
from typing import List, Optional
class User(BaseModel):
    username: str
    password: str
    email: str
    assigned_items: Optional[List[str]] = []
