from fastapi import FastAPI, HTTPException

app = FastAPI()
# if you name it myapp then uvicorn main:myapp --reload
# if you name it index.py then uvicorn index:app --reload
# so these two parameters what you name the instace and name of the file are very important


@app.get("/")
async def root():
    return {"message": "Shree Ganesh!",        
    "sonOf":
    {
        "father":"shri mahadev",
        "mother": "shri parvati"
    }
    }

@app.get("/about")
async def root():
    return {
        "bitFumes":"Youtube for Coding",
}

# 4 things to be done
# import fastapi
# instance
# function
# decorate

