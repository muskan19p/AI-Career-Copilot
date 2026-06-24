from passlib.context import CryptContext
from jose import JWTError, jwt
import datetime
import os

SECRET = os.getenv("SECRET_KEY", "career_os_secret")

pwd = CryptContext(schemes=["bcrypt"])

def hash_password(p):
    return pwd.hash(p)

def verify_password(p, h):
    return pwd.verify(p, h)

def create_access_token(data):
    payload = data.copy()
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    return jwt.encode(payload, SECRET, algorithm="HS256")

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except JWTError:
        return None
    
    