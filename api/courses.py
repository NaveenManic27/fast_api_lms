
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


@router.get("/courses")
async def read_courses():
    return {"courses": []}

@router.post("/courses")
async def create_user(user:User):
    users.append(user)
    return {"courses": []}

@router.get("/courses/{id}")
async def read_course():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_course( id:int ): 
    return {"courses": []}

@router.patch("/users/{id}")
async def update_course( id:int ): 
    return {"courses": []}

@router.get("/courses/{id}/sections")
async def read_courses_sections( id:int ): 
    return {"courses": []}

@router.get("/courses/{id}/sections")
async def read_courses_sections( id:int ): 
    return {"courses": []}

@router.get("/sections/{id}")
async def read_sections( id:int ): 
    return {"courses": []}

@router.get("/sections/{id}/content-blocks")
async def read_sections_content_blocks( id:int ): 
    return {"courses": []}