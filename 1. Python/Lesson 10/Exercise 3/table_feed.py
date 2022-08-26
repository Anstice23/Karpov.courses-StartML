from database import Base
from table_user import User
from table_post import Post
from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship


class Feed(Base):
    __tablename__ = "feed_action"
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    action = Column(Text)
    time = Column(DateTime)
    user = relationship("User")
    post = relationship("Post")

