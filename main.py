from fastapi import FastAPI
from routes import users, items, locations

app = FastAPI()

app.include_router(users.router, tags=["Users"])
app.include_router(items.router, tags=["Items"])
app.include_router(locations.router, tags=["Locations"])
