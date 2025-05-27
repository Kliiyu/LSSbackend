from fastapi import APIRouter
from models.stored import Stored
from database import db, fix_mongo_ids

router = APIRouter()

@router.get("/stored")
async def get_items():
    stored = await db.stored.find().to_list(100)
    return fix_mongo_ids(stored)

# TODO: post new stored item, put more quantity