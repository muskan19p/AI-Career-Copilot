from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.core.database import Base

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    goal = Column(String)
    completion = Column(Integer)