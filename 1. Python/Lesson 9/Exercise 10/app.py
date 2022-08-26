from fastapi import FastAPI, HTTPException, Depends
# from pydantic import BaseModel
import psycopg2.extras
import psycopg2

app = FastAPI()


async def get_db():
    conn = psycopg2.connect(
        'postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml')
    return conn

@app.get('/user/{id}')
def my_func(id, db = Depends(get_db)):
    with db.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute(
        f"""
        SELECT gender, age, city
        FROM "user"
        WHERE id = {id}
        """
)
        result = cursor.fetchone()
    if result is None:
        raise HTTPException (status_code=404, detail="user not found")
    else:
        return result
