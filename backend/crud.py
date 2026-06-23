from sqlalchemy.orm import Session
from backend.models import User
from backend.auth import hash_password, verify_password

# REGISTER
def create_user(db: Session, name: str, email: str, password: str):

    email = email.strip().lower()

    user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# LOGIN
def get_user_by_email(db: Session, email: str):

    email = email.strip().lower()

    return db.query(User).filter(
        User.email == email
    ).first()


def authenticate_user(db: Session, email: str, password: str):

    user = get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user