from typing import Union
from fastapi import FastAPI
from router import router

app = FastAPI()

app.include_router(router)


@app.get("/users/{id}")
def user_id(id: str):
    return {"id": id}

@app.get("/users/name/{name}")
def user_id(name: str):
    return {"name": name}

@app.get("/policies/{user_name}")
def user_id(user_name:str):
    return {"user_name": user_name}

@app.get("/policies/{number}/user/")
def user_id(number: str):
    return {"policy_number": number}
