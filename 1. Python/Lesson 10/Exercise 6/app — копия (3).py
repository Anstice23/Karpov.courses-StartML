from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from database import SessionLocal
from schema import UserGet, PostGet, FeedGet
from table_user import User
from table_post import Post
from table_feed import Feed
from pydantic import BaseModel

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

@app.get('/user/{id}/feed', response_model=List[FeedGet])
def get_user_feed(id, limit: int = 10, db: Session = Depends(get_db)) -> FeedGet:
    return db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()


@app.get('/post/{id}/feed', response_model=List[FeedGet])
def get_post_feed(id, limit: int = 10, db: Session = Depends(get_db)) -> FeedGet:
    return db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()


