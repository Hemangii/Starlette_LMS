import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from db.db_setup import Base



class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)

    def as_json(self):
         return { "id" : self.id,
                 "name": self.name}


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)

    


    def as_json(self):
            return { "id" : self.id,
                    "email" : self.email ,
                  
                    "first_name": self.first_name,
                    "last_name": self.last_name
               
                }




class UserRoleMapper(Base):
    __tablename__ = "user_role_mapper"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, ForeignKey("users.id"), nullable=False)
    role = Column(String, ForeignKey("roles.id"), nullable=False)

    def as_json(self):
            return { "id" : self.id,
                    "user" : self.user,
                    "user_name": self.user,
                  
                    
                    "role": self.role
               
                }
    
     