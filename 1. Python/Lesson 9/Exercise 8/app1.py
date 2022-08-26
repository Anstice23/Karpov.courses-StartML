from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
import psycopg2.extras
import psycopg2

app = FastAPI()


@app.get("/user/{id}")
def user_id(id):
    conn = psycopg2.connect(
        'postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml')

    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
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
