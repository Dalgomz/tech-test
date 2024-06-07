from typing import Union
from fastapi import APIRouter, HTTPException

import repository
import service

router = APIRouter()

@router.get("/users/{id}")
def user_id(id: str):
    return service.get_user_by_id(id)

@router.get("/users/name/{name}")
def user_id(name: str):
    return service.get_user_by_name(name)

@router.get("/policies/{user_name}")
def user_id(user_name:str):
    return service.get_policy_by_user(user_name)

@router.get("/policies/{number}/user/")
def user_id(number: str):
    return service.get_policy_owner(number)