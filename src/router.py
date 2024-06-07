from typing import Union
from fastapi import APIRouter, HTTPException

import repository
import service

router = APIRouter()

def get_user_by_id(id: str, uid: Union[str, None] = None):
    if repository.auth_user(uid, ['user', 'admin']):
        return service.get_user_by_id(id)
    raise HTTPException(403, detail="Unauthorized user")

@router.get("/users/name/{name}")
def get_user_by_name(name: str, uid: Union[str, None] = None):
    if repository.auth_user(uid, ['user', 'admin']):
        return service.get_user_by_name(name)
    raise HTTPException(403, detail="Unauthorized user")

@router.get("/policies/{username}")
def get_policy_by_username(username: str, uid: Union[str, None] = None):
    if repository.auth_user(uid, ['admin']):
        return service.get_policy_by_user(username)
    raise HTTPException(403, detail="Unauthorized user")

@router.get("/policies/{number}/user/")
def get_policy_owner(number: str, uid: Union[str, None] = None):
    if repository.auth_user(uid, ['admin']):
        return service.get_policy_owner(number)
    raise HTTPException(403, detail="Unauthorized user")
