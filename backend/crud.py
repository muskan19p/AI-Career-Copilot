from sqlalchemy.orm import Session

from backend.models import User
from backend.auth import hash_password
from backend.models import ResumeHistory

def create_user(
        db: Session,
        name: str,
        email: str,
        password: str
):

    user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )
    
def get_user_by_email(
        db,
        email
):

    return db.query(User).filter(
        User.email == email
    ).first()
    
def save_resume_analysis(
        db,
        user_id,
        resume_text,
        analysis
):

    record = ResumeHistory(
        user_id=user_id,
        resume_text=resume_text,
        analysis=analysis
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record

def get_user_history(
        db,
        user_id
):

    return db.query(
        ResumeHistory
    ).filter(
        ResumeHistory.user_id == user_id
    ).all()
    
def delete_history(
        db,
        history_id
):

    record = db.query(
        ResumeHistory
    ).filter(
        ResumeHistory.id == history_id
    ).first()

    if not record:
        return False

    db.delete(record)

    db.commit()

    return True

    db.add(user)

    db.commit()

    db.refresh(user)

    return user
