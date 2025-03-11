from fastapi import FastAPI, Depends, Response
from http import HTTPStatus
from database import get_db


app = FastAPI()


@app.get('/')
def root(db=Depends(get_db)):
    return Response(status_code=HTTPStatus.OK)