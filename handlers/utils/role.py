from sqlalchemy.orm import Session
from sqlalchemy import engine
from db.db_setup import get_db
from handlers.utils.models.user import *


# db=Session()
def get_role(db: get_db(), role_id: int):
    role= db.query(Role).filter(Role.id == role_id).first()
    if role is None:
        raise Exception(status_code=404, detail="Role not found")
    return role.as_json()


def get_role_by_name(db: Session, name: str):
    return db.query(Role).filter(Role.name == name).first()


def get_roles(db: Session, skip: int = 0, limit: int = 100):
    roles=db.query(Role).all()
    return [role.as_json() for role in roles]


def create_role(db: Session, name: str):
    db_role = Role(name=name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return Role.as_json(db_role)

def add_user_role(db:Session, role_id, user_id):
    db_user_role= UserRoleMapper(role= role_id, user= user_id)
    db.add(db_user_role)
    db.commit()
    db.refresh(db_user_role)
    return UserRoleMapper.as_json(db_user_role)
