from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI

app = FastAPI()


#connection to sqlite_database
sqlite_database = "sqlite:///test.db"


#Creating engine SqlAlchemy
engine = create_engine(sqlite_database,connect_args={"echo":False})



#Creating class of Session
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()







