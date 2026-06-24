from fastapi import Header, HTTPException
from backend.app.core.security import decode_token

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No token")

    token = authorization.split(" ")[1]
    user = decode_token(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user