from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def showBlogList():
    return {"data":"list_of_blogs"}


# In this tutorial we will learn about CRUD operations
# Create, Read, Update, Delete
# post, get, put, delete

# @app.post("/blog")
# async def createBlog():
#     return {"data":f'Blog created with id 10'}


class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool] 

@app.post("/blog")
async def createBlog(request:Blog):
    return request
    