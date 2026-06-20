from pydantic import BaseModel


class UserCreate(BaseModel):

    name: str
    email: str
    password: str
    
class UserLogin(BaseModel):

    email: str
    password: str
    
class ResumeSave(BaseModel):

    user_id: int
    resume_text: str
    analysis: str