from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def showBlogList():
    return {"data":"list_of_blogs"}

# @app.get("/blog/{id}")
# async def show_Nth_Blog(id:int):
#         # fetch blog with id = id
#     return {"data":id}

# # List of all unpublished blogs
# @app.get("/blog/unpublished")
# async def show_Nth_Blog(id:str):
#         # fetch blog with id = id
#     return {"data":id}


# output
# http://localhost:8000/blog/unpublished
# gives me an error
'''{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "unpublished"
    }
  ]
}'''
# Why because fastapi see there is somthing after blog/ and when it executes line by line it sees that blog/id is such a route it never reaches blog/unpublished as a route and thus gives as error as it assumes the funtion wihch we are talking about is the third function and not the third function

# so how to solve this problem
# in such conflicting cases always prefer to take the dynamic routes below the non-dynamic routes

# List of all unpublished blogs
@app.get("/blog/unpublished")
async def show_Nth_Blog(id:str):
        # fetch blog with id = id
    return {"data":id}


@app.get("/blog/{id}")
async def show_Nth_Blog(id:int):
        # fetch blog with id = id
    return {"data":id}