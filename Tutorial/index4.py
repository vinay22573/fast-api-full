from typing import Optional 
from fastapi import FastAPI, HTTPException

app = FastAPI()

# In this tutorial we learn about Query parameters
# @app.get("/")
# async def showBlogList():
#     return {"data":"list_of_blogs"}




# @app.get("/blog/unpublished")
# async def show_Nth_Blog(id:str):
#         # fetch blog with id = id
#     return {"data":id}

# Query Parameters ==> ?name1=value1&name2=value2
# @app.get('/blog')
# async def show_Nth_Blog(limit,published):
#         # fetch blog with id = id
#     return {"data":f'{limit} published blogs and {published} unpublished blogs'}




# @app.get('/blog')
# async def show_Nth_Blog(limit = 10,published:bool = True):
#         # fetch blog with id = id
#     if published:
#         return {"data":f'{limit} published blogs'}
#     else:
#         return {"data":f'{limit} blogs from the db'}


# But what if some Query parameters are not required and some are required
# use of Optional
@app.get('/blog')
async def show_Nth_Blog(limit:int = 10, published:bool = True, sort:Optional[str] = None):
        # fetch blog with id = id
    if published:
        return {"data":f'{limit} published blogs'}
    else:
        return {"data":f'{limit} blogs from the db'}
    
# Here in the given below examplethe id is path parameter and limit is query parameter why because id is present in path whereas limit is only present in function arguments
@app.get('/blog/{id}/comments')
async def comments(id:int=10, limit:int = 10,):
    return {"data":f'{limit} comments for blog {id}'}
# since we have not given any value for id why does it not gives an error
# Because fastapi is smartenough to understand that this is a path parameter and it will not go to the query parameter and thus it will not give an error

