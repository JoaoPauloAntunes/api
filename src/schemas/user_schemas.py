from typing import List, Optional
from pydantic import BaseModel, EmailStr

from .requisition_schemas import Requisition


"""
  id
  email
  hashed_password
  is_active

  requisitions
"""
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: Optional[int] = None
    requisitions: List[Requisition] = []

    class Config:
        orm_mode = True
