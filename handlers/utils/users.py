from sqlalchemy.orm import Session
from sqlalchemy import engine
from db.db_setup import get_db
from handlers.utils.models.user import *
from pydantic_schemas.user import UserCreate

# db=Session()
def get_user(db: get_db(), user_id: int):
    
    user=db.query(User).filter(User.id == user_id).first()
    return user.as_json()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    users=db.query(User).all()
    return [ user.as_json() for user in users]


def create_user(db: Session, user: User):
    db_user = User(first_name=user.first_name, last_name=user.last_name,email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return User.as_json(db_user)