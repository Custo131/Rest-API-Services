from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 
from pydantic import BaseModel






#connect to a SQLite database stored in a file called test.db
sqlite_url = "sqlite:///test.db"


#Creating engine for providing connection to database
engine = create_engine(sqlite_url,connect_args={"check_same_thread":False})




SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Creating basic class for models
Base = declarative_base()

#Defining the model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,   index=True)
    email = Column(String, unique=True, index=True)





#Defining Pydantic model for validating data
class UserCreate(BaseModel):
    name: str
    email: str


#Creating tables if they're not existing 
Base.metadata.create_all(bind=engine)








 








