from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from database import SessionLocal
from schema import UserGet, PostGet, FeedGet
from table_user import User
from table_post import Post

app = FastAPI()

def get_db():
    with SessionLocal() as db:
        return db

@app.get('/user/{id}', response_model=UserGet)
def get_user_id(id, db: Session = Depends(get_db)) -> UserGet:
    try:
        return db.query(User).filter(User.id==id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="user not found")

@app.get('/post/{id}', response_model=PostGet)
def get_post_id(id, db: Session = Depends(get_db)) -> PostGet:
    try:
        return db.query(Post).filter(Post.id==id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="post not found")


