from pydantic import BaseModel
from uuid import UUID

class ProfileCreate(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class ProfileResponse(ProfileCreate):
    user_id: UUID
    email: str
