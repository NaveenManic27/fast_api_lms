from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query

app = FastAPI(
    title="FAST API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name":"Naveen",
        "email": "naveenmanic@gmail.com"
    },
    license_info = {"name": "MIT"},
    
)


users = []

class User(BaseModel):
    email: str
    is_active : bool
    bio:Optional[str]

@app.get("/users", response_model = List[User])
async def get_user():
    return users

@app.post("/users")
async def create_user(user:User):
    users.append(user)
    return "success"

@app.get("/users/{id}")
async def get_desired_users(
    id:int = Path(..., description="The Id of the user you want to retrieve ", gt=1),
    q : str = Query(None, max_length=5) ): # we can also use is_active : bool = Query(None, max_length = 5)
    return {"user":users[id], "query":q}