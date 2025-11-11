from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def showBlogList():
    return {"data":"list_of_blogs"}

# @app.get("/blogs")
# async def show_Nth_Blog():
#     return {"data":"list_of_blogs"}
# I want to create this function where whatever blog id i give that blog should open up if i give id=1 then 1st blog should open up now how to do it


# # Dynamic Routing
# @app.get("/blog/{id}")
# async def show_Nth_Blog(id):
#         # fetch blog with id = id
#     return {"data":id}


# @app.get("/blog/{id}/comments")
# async def show_Nth_blog_comments(id):
#         # fetch comments of blog of id = id
#     return { 'data':{'1','2'} }

# Learnings from this always have /at the start


# # Type Defining
# @app.get("/blog/{id}")
# async def show_Nth_Blog(id:int):
#         # fetch blog with id = id
#     return {"data":id}


# Deliberately fill  this and see the effect --> http://localhost:8000/blog/my_first_error_full_blog
# @app.get("/blog/{id}")
# async def show_Nth_Blog(id:int):
#         # fetch blog with id = id
#     return {"data":id}


# # output = {
# #   "detail": [
# #     {
# #       "type": "int_parsing",
# #       "loc": [
# #         "path",
# #         "id"
# #       ],
# #       "msg": "Input should be a valid integer, unable to parse string as an integer",
# #       "input": "my_first_blog"
# #     }
# #   ]
# # }





# @app.get("/blog/{id}")
# async def show_Nth_Blog(id:str):
#         # fetch blog with id = id
#     return {"data":id}


