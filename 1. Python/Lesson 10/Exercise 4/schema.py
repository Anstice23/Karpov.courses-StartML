import datetime

from pydantic import BaseModel


class PostGet(BaseModel): 

    id: int
    text: str = ""
    topic: str = ""

    class Config:
        orm_mode = True
        
class UserGet(BaseModel):

    id: int
    gender: int
    age: int
    country: str = ""
    city: str = ""
    exp_group: int
    os: str = ""
    source: str = ""

    class Config:
        orm_mode = True

class FeedGet(BaseModel):
    user_id: int
    user: UserGet
    post: PostGet
    user_id: int
    post_id: int
    action: str = ""
    time: datetime.datetime

    class Config:
        orm_mode = True