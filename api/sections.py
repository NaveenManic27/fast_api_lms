
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

@router.get("/sections/{id}", response_model = list[User])
async def read_section():
    return {"courses":[]}

@router.post("/sections/{id}/content-blocks")
async def read_section_content_blocks():
    return {"courses":[]}

@router.get("/content-blocks/{id}")
async def read_content_block(): 
    return {"courses":[]}