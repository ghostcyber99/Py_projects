from pyrsistent import optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

#validating user input
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int = None

#saving the post
my_posts = [{"title": "title of post 1", "content": "content of post1", "id": 1}, {"title": "favorite foods", "content": "i love yam", "id": 2} ]



#get method 
@app.get("/")
def read_root():
    return {"message": "welcome to my api"}

#Post method
@app.get("/posts")
def get_posts():
    return{"data": my_posts}

@app.post("/posts")
def create_posts(post: Post): #
    print( post.rating)
    return{"data": "new_post"}


