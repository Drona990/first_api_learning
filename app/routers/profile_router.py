from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.profile_controller import create_or_update_profile, get_profile
from app.schemas.profile_schema import ProfileCreate, ProfileResponse
from app.utils.security import get_current_user

router = APIRouter(prefix="/api/v1/profiles", tags=["Profiles"])

@router.post("/createProfile", response_model=ProfileResponse)
def create_user_profile(
    profile: ProfileCreate, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    return create_or_update_profile(db, current_user["user_id"], current_user["email"],profile)

@router.get("/getProfile", response_model=ProfileResponse)
def get_user_profile(
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    return get_profile(db, current_user["user_id"])
