from fastapi import FastAPI
from app.routers.auth_router import router as auth_router
from app.models.user_model import Base
from app.database import engine
from app.routers.profile_router import router as profile_router


app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router)
app.include_router(profile_router)

