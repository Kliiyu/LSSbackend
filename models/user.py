from pydantic import BaseModel, EmailStr
from typing import List, Optional
from bson import ObjectId

class User(BaseModel):
    username: str
    email: EmailStr
    assigned_items: Optional[List[str]] = []
