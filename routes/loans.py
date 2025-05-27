from fastapi import APIRouter
from models.loaned import Loaned
from database import db, fix_mongo_ids

router = APIRouter()

@router.get("/loans")
async def get_items():
    loans = await db.loans.find().to_list(100)
    return fix_mongo_ids(loans)

@router.post("/loans")
async def create_item(loan: Loaned):
    result = await db.loans.insert_one(loan.dict())
    return {"inserted_id": str(result.inserted_id)}

@router.put("/loans/{loan_id}/assign_user")
async def assign_user(load_id: str, user_id: str):
    result = await db.items.update_one(
        {"_id": load_id}, {"$set": {"assigned_user": user_id}}
    )
    return {"matched": result.matched_count, "modified": result.modified_count}
