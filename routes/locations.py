from fastapi import APIRouter
from models.location import Location
from database import db

router = APIRouter()

@router.get("/locations")
async def get_locations():
    return await db.locations.find().to_list(100)

@router.post("/locations")
async def create_location(location: Location):
    result = await db.locations.insert_one(location.dict())
    return {"inserted_id": str(result.inserted_id)}
