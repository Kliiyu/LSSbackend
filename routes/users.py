from fastapi import APIRouter
from models.user import User
from database import db

router = APIRouter()

@router.get("/users")
async def get_users():
    users = await db.users.find().to_list(100)
    return users

@router.post("/users")
async def create_user(user: User):
    result = await db.users.insert_one(user.dict())
    return {"inserted_id": str(result.inserted_id)}
