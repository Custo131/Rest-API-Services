from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, User, UserCreate

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Hello World"}













