from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

#validating user input
class Post(BaseModel):
    title: str
    content: str

#get method 
@app.get("/")
def read_root():
    return {"message": "welcome to my api"}

#Post method
@app.get("/posts")
def get_posts():
    return{"data": "This is your post "}

@app.post("/createposts")
def create_posts(new_post: Post): #
    print(new_post)
    return{"data": "new_post"}


