from fastapi import APIRouter
from models.item import Item
from database import db, fix_mongo_ids

router = APIRouter()

@router.get("/items")
async def get_items():
    items = await db.items.find().to_list(100)
    return fix_mongo_ids(items)

@router.post("/items")
async def create_item(item: Item):
    result = await db.items.insert_one(item.dict())
    return {"inserted_id": str(result.inserted_id)}

@router.put("/items/{item_id}/assign_user")
async def assign_user(item_id: str, user_id: str):
    result = await db.items.update_one(
        {"_id": item_id}, {"$set": {"assigned_user": user_id}}
    )
    return {"matched": result.matched_count, "modified": result.modified_count}
