from typing import List, Optional
from pydantic import BaseModel, EmailStr
# from datetime import datetime

# from sqlalchemy.sql.sqltypes import Date, DateTime

""" 
  reqn
  file_url
  time_updated
  progress_level
  is_free
  owner_id
"""
class RequisitionBase(BaseModel):
    file_url: Optional[str] = None
    progress_level: Optional[float] = None
    is_free: Optional[bool] = True

class RequisitionCreate(RequisitionBase):
    file_url: str
    progress_level: float


class RequisitionUpdate(RequisitionBase):
    pass


class Requisition(RequisitionBase):
    reqn: int
    owner_id: int

    class Config:
        orm_mode = True