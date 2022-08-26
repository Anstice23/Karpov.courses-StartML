from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()
@app.post('/user/validate')
class User (BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date   