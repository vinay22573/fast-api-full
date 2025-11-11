from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel


app = FastAPI()
class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]

@app.get('/')
def home():
    return {"Home": "Welcome to FastAPI"}

@app.post('/blog')
def create_blog(request: Blog):
    return {"data": "Blog created with title: {}".format(request.title)}

