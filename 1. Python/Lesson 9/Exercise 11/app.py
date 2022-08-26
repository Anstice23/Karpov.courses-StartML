from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2.extras
import psycopg2

app = FastAPI()

class PostResponse (BaseModel):
    id: int
    text: str
    topic: str
    class Config:
        orm_mode = True
            
async def get_db():
    conn = psycopg2.connect(
        'postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml')
    return conn

@app.get('/post/{id}', response_model=PostResponse)
def my_func(id, db = Depends(get_db)) -> PostResponse:
    with db.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute(
        f"""
        SELECT id, text, topic
        FROM "post"
        WHERE id = {id}
        """
)
        result = cursor.fetchone()
    if result is None:
        raise HTTPException (status_code=404, detail="user not found")
    else:
        return PostResponse(**result)
