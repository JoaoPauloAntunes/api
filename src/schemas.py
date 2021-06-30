from typing import List, Optional

from pydantic import BaseModel, EmailStr


class RequisitionBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
# file_url
# date
# progress_level
# is_free
# owner_id
# owner

class RequisitionCreate(RequisitionBase):
    file_url: str
    


class RequisitionUpdate(RequisitionBase):
    owner_id: Optional[int] = None


class Requisition(RequisitionBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


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
