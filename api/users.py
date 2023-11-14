
from typing import Optional, List
import fastapi
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query


router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active : bool
    bio:Optional[str]

@router.get("/users", response_model = list[User])
async def get_users():
    return users

@router.post("/users")
async def create_user(user:User):
    users.append(user)
    return "success"

@router.get("/users/{id}")
async def get_desired_users( id:int ): 
    return {"user":users[id]}