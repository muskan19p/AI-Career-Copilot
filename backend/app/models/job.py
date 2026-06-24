from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.core.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String)
    company = Column(String)
    status = Column(String)