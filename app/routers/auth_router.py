from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.auth_controller import signup, login
from app.schemas.auth_schemas import UserCreate, Token ,UserResponse

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

@router.post("/signup", response_model=UserResponse)
def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    return signup(db, user)

@router.post("/login", response_model=Token)
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    return login(db, user.email, user.password)
