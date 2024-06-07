from typing import Union
from fastapi import APIRouter, HTTPException

import service

router = APIRouter()

def get_user_by_id(id: str, uid: Union[str, None] = None):
    if not service.auth_user(uid, ['user', 'admin']) or uid is None:
        raise HTTPException(403, detail="Unauthorized user")
    return service.get_user_by_id(id)

@router.get("/users/name/{name}")
def get_user_by_name(name: str, uid: Union[str, None] = None):
    if not service.auth_user(uid, ['user', 'admin']) or uid is None:
        raise HTTPException(403, detail="Unauthorized user")
    return service.get_user_by_name(name)

@router.get("/policies/{username}")
def get_policy_by_username(username: str, uid: Union[str, None] = None):
    if not service.auth_user(uid, ['admin']) or uid is None:
        raise HTTPException(403, detail="Unauthorized user")
    return service.get_policy_by_user(username)

@router.get("/policies/{number}/user/")
def get_policy_owner(number: str, uid: Union[str, None] = None):
    if not service.auth_user(uid, ['admin']) or uid is None:
        raise HTTPException(403, detail="Unauthorized user")
    return service.get_policy_owner(number)
