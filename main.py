import json
from fastapi import FastAPI
from tasks import create_user_task, update_user_task, get_user_task

app = FastAPI()

@app.get("/create_user")
async def create_user_route(db_file: str, age: int, income: int, physiological_need: str, safety_need: str, love_and_belonging_need: str, esteem_need: str, self_actualization_need: str):
    promise = create_user_task.delay(db_file=db_file, age=age, income=income, physiological_need=physiological_need, safety_need=safety_need, love_and_belonging_need=love_and_belonging_need, esteem_need=esteem_need, self_actualization_need=self_actualization_need)
    result = promise.get()
    return json.dumps({"id": result})

@app.get("/update_user")
async def update_user_route(db_file="user.db", user_id="username", age=None, income=None, physiological_need=None, safety_need=None, love_and_belonging_need=None, esteem_need=None, self_actualization_need=None):
    promise = update_user_task.delay(db_file=db_file,user_id=user_id ,age=age,income=income ,physiological_need=physiological_need,safety_need=safety_need ,love_and_belonging_need=love_and_belonging_need ,esteem_need=esteem_need,self_actualization_need=self_actualization_need)
    result = promise.get()
    if result == "SUCCESS":
        return 200

@app.get("/get_user")
async def get_user_route(db_file:str,user_id:str):
    promise = get_user_task.delay(db_file=db_file,user_id=user_id)
    result = promise.get()
    return json.dumps(result)