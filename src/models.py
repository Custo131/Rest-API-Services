
from sqlalchemy.orm import DeclarativeBase
from src.database import engine
from sqlalchemy import Column,String,  Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

class Base (DeclarativeBase):
    pass


Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = "users"
    _id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(150))
    created_at = Column(DateTime, default=func.now())
    
    
