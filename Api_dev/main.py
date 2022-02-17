from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return{"data": "This is your post "}

