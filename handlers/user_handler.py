from os import stat
from typing import Optional, List

from sqlalchemy.orm import Session
from starlette.requests import Request
from db.db_setup import get_db
from pydantic_schemas.user import UserCreate, User
from starlette.responses import JSONResponse
from handlers.utils.users import *




async def read_users(skip: int = 0, limit: int = 100, db: Session = (get_db())):
    users = get_users(db, skip=skip, limit=limit)
    return JSONResponse({"users" :users})



async def create_new_user(request:Request ,  db: Session = (get_db())):
    
    try:
        data = await request.json()
        
    except RuntimeError:
         data = "Receive channel not available"
    
    user= User(**data)
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise Exception(status_code=400, detail="Email is already registered")
    return JSONResponse({"user" : (create_user(db=db, user=user)) })



async def read_user(request: Request, db: Session = (get_db())):
    user_id= request.path_params.get("user_id")
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise Exception(status_code=404, detail="User not found")
    return JSONResponse({"user" : db_user})



async def read_user_courses(user_id: int, db: Session = (get_db())):
    courses = get_user_courses(user_id=user_id, db=db)
    return courses