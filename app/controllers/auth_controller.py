from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth_schemas import UserCreate, Token
from app.services.auth_services import signup_user, login_user

def signup(db: Session, user: UserCreate):
    return signup_user(db, user)

def login(db: Session, email: str, password: str):
    token = login_user(db, email, password)
    return {"access_token": token, "token_type": "Bearer"}
