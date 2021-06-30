from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Float
from sqlalchemy.orm import relationship
# import datetime
from sqlalchemy.sql import func

from ..database import Base

class Requisition(Base):
    __tablename__ = "requisitions"

    reqn = Column(Integer, primary_key=True, index=True) # alterar o tipo para UUID
    file_url = Column(String, index=True)
    time_updated = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    progress_level = Column(Float)
    is_free = Column(Boolean)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="requisitions")