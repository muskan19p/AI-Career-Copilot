from pydantic import BaseModel

class UserOut(BaseModel):
    name: str
    email: str