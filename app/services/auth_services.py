from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repository import get_user_by_email, create_user
from app.schemas.auth_schemas import UserCreate
from app.utils.security import hash_password, verify_password, create_access_token

def signup_user(db: Session, user: UserCreate):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user.password = hash_password(user.password)
    return create_user(db, user)

def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return create_access_token({"user_id": str(user.user_id), "email": user.email})
