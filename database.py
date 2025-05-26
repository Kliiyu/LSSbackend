from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

from config import MONGO_URI, DATABASE_NAME

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

def fix_mongo_ids(doc):
    """
    Recursively convert ObjectId to str in MongoDB documents
    """
    if isinstance(doc, list):
        return [fix_mongo_ids(d) for d in doc]
    if isinstance(doc, dict):
        return {
            k: fix_mongo_ids(v)
            for k, v in doc.items()
        }
    if isinstance(doc, ObjectId):
        return str(doc)
    return doc