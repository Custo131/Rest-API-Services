from fastapi import FastAPI, Depends, Response
from http import HTTPStatus
from src.database import get_db
from routes import router 




app = FastAPI()

app.include_router(router)



@app.get('/')
def root(db=Depends(get_db)):
    return Response(status_code=HTTPStatus.OK)
