from sqlalchemy import Column, Integer, Text, ForeignKey
from backend.app.core.database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    ats_score = Column(Integer)