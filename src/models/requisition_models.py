from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from .database import Base
import datetime

class Requisition(Base):
    __tablename__ = "requisitions"

    reqn = Column(Integer, primary_key=True, index=True) # alterar o tipo para UUID
    file_url = Column(String, unique=True, index=True)
    last_modified = Column(DateTime, onupdate=datetime.datetime.now) # define to be populated with datetime.now()
    progress_level = Column(Float)
    is_free = Column(Boolean)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="requisitions")