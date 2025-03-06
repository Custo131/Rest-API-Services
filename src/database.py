from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase


#connect to a SQLite database stored in a file called test.db
sqlite_url = "sqlite:///test.db"


## Create the engine and sessionmaker
engine = create_engine(sqlite_url,connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



#Declarative base for ORM models
Base = DeclarativeBase()

# 
def init_db():
    Base.metadata.create_all(bind=engine)



#Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






















 








