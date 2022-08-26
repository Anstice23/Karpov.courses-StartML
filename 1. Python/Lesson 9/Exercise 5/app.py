from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get('/sum_date')
def sum_date(current_date: datetime.date, offset: int) -> datetime.date:
    return current_date + datetime.timedelta(offset)
