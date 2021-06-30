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

class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None
    is_active: Optional[bool] = True


class User(UserBase):
    id: Optional[int] = None
    is_active: bool = True
    requisitions: List[Requisition] = []

    class Config:
        orm_mode = True
