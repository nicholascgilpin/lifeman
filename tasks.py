import os
from celery import Celery
from database import create_user, update_user, get_user

app = Celery(
                'tasks', 
                broker='redis://localhost', 
                backend='redis://localhost'
            )

def add(x, y):
    return x + y

@app.task
def create_user_task(db_file: str, age: int, income: int, physiological_need: str, safety_need: str, love_and_belonging_need: str, esteem_need: str, self_actualization_need: str):
    return create_user(db_file=db_file, age=age, income=income, physiological_need=physiological_need, safety_need=safety_need, love_and_belonging_need=love_and_belonging_need, esteem_need=esteem_need, self_actualization_need=self_actualization_need)

@app.task
def update_user_task(db_file="user.db", user_id="username", age=None, income=None, physiological_need=None, safety_need=None, love_and_belonging_need=None, esteem_need=None, self_actualization_need=None):
    return update_user(db_file=db_file,user_id=user_id ,age=age,income=income ,physiological_need=physiological_need,safety_need=safety_need ,love_and_belonging_need=love_and_belonging_need ,esteem_need=esteem_need,self_actualization_need=self_actualization_need)

@app.task
def get_user_task(db_file:str,user_id:str):
    return get_user(db_file=db_file,user_id=user_id)