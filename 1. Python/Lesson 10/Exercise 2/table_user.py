
from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    gender = Column(Integer)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    exp_group = Column(Integer)
    os = Column(String)
    source = Column(String)


if __name__ == '__main__':
    session = SessionLocal()
    
    result = []
    for row in (
        session.query(User.country, User.os, func.count('*').label('count'))
        .filter(User.exp_group == 3)
        .group_by(User.country, User.os)
        .having(func.count('*') > 100)
        .order_by(func.count('*').desc())
        .all()
    ):
        result.append((row.country, row.os, row.count))
    print(result)


#     result = session.execute(row).fetchone()
# result