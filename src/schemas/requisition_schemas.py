from typing import List, Optional
from pydantic import BaseModel, EmailStr


""" 
  reqn
  file_url
  last_modified
  progress_level
  is_free
  owner_id
"""
class RequisitionBase(BaseModel):
    file_url: Optional[str] = None
    progress_level: Optional[float] = None


class RequisitionCreate(RequisitionBase):
    file_url: str
    progress_level: float
    is_free: bool


class RequisitionUpdate(RequisitionBase):
  # last_modified: str
  pass


class Requisition(RequisitionBase):
    reqn: int
    owner_id: int

    class Config:
        orm_mode = True