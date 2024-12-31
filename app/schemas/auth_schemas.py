from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    user_id: UUID

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserResponse(BaseModel):
    user_id: UUID
    email: str

class TokenData(BaseModel):
    email: str | None = None
