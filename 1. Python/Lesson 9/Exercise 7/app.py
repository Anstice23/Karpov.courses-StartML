from fastapi import FastAPI
from pydantic import BaseModel

import datetime

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date 
    
    class Cofig:
        orm_mode = True

@app.post('/user/validate') 
def user_validate(user: User):

    return f'Will add user: {user.name} {user.surname} with age {user.age}'