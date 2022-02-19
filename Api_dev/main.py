from turtle import pos
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

#validating user input
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

#saving the post
my_posts = [{"title": "title of post 1", "content": "content of post1", "id": 1}, {"title": "favorite foods", "content": "i love yam", "id": 2} ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p 

#get method 
@app.get("/")
def read_root():
    return {"message": "welcome to my api"}

#Post method
@app.get("/posts")
def get_posts():
    return{"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):   
    post_dict = post.dict() #creatig a brand new post from the pydantic dictionary 
    post_dict['id'] = randrange(0, 10000000) #assign the id in the dict with a random number 
    my_posts.append(post_dict) #converting pydantic model to a dictionary and appeding it to an array
    return{"data": post_dict}

#calling a particular post id 
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found ")
    return{"post_details": post}
