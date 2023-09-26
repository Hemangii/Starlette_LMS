from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
import os

BASE_DIR= os.path.dirname(os.path.realpath(__file__))
conn_str= os.path.join(BASE_DIR, "lms.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{conn_str}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

Base = declarative_base()

# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()