from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        'data':'blog list'
    }

# @app.get('/blog?limit=10&published=true')# this will hardcode the query parameters
# we don't want that instead we want to make it dynamic
# so we will use query parameters in the function definition
@app.get("/blog")
def top_ten(limit):
    return {
        'data':f'top {limit} blogs'
    }

# Endpoints with Query Parameters
def qp_example(limit,published:bool):
    if published:
        return {
            'data':f'top {limit} published blogs'
        }
    else: 
        return {
            'data':f'top {limit} blogs'
        }


@app.get("/blog/unpublished")
def unpublished():
    return {
        'data':'all unpublished blogs'
    }

