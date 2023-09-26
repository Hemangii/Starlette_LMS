
from typing import Optional, List

from sqlalchemy.orm import Session
from starlette.requests import Request
from db.db_setup import get_db
from pydantic_schemas.user import UserCreate, User
from starlette.responses import JSONResponse
from handlers.utils.role import *
from starlette.requests import Request




async def read_roles(request:Request ,db: Session = (get_db())):
    roles = get_roles(db)
    return JSONResponse({"roles" :roles})



async def create_new_role(request:Request, db: Session = (get_db())):
    
    try:
        data = await request.json()
        
    except RuntimeError:
         data = "Receive channel not available"
    
    
    db_role = get_role_by_name( db=db, name= data.get("name"))
    if db_role:
        raise Exception(status_code=400, detail="Role is already present")
    return JSONResponse({"role" : (create_role(db=db, name=data.get("name"))) })



async def read_role(request:Request , db: Session = (get_db())):
    role_id= request.path_params.get("role_id")
    db_role = get_role(db=db, role_id=role_id)
    
    return JSONResponse({"role" : db_role })

async def add_user_roles(request:Request,  db :Session = (get_db())):
    
    
        
        role_id= request.path_params.get("role_id")
        user_id= request.path_params.get("user_id")
        result= add_user_role(db=db, role_id=role_id, user_id=user_id)
        return JSONResponse({"role" : result })
   
    





