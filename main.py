from fastapi import FastAPI
from routes import loans, users, locations, stored

app = FastAPI()

app.include_router(users.router, tags=["Users"])
app.include_router(loans.router, tags=["Loans"])
app.include_router(stored.router, tags=["Stored"])
app.include_router(locations.router, tags=["Locations"])
