
from distutils.log import error
from operator import index
from turtle import pos
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time 

app = FastAPI()

#validating user input
class Post(BaseModel): 
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Smith3dx', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print(" database connected ")
        break
    except Exception as error:
        print("Connection failure")
        print("Error: ", error)
        time.sleep(2)    

#saving the post
my_posts = [{"title": "title of post 1", "content": "content of post1", "id": 1}, {"title": "favorite foods", "content": "i love yam", "id": 2} ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p 


def find_index_post(id):
    for i , p in enumerate(my_posts):
        if p['id'] == id:
            return i

#get method 
@app.get("/")
def read_root():
    return {"message": "welcome to my api"}

#Post method
@app.get("/posts")
def get_posts():
    return{"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):   
    post_dict = post.dict() #creatig a brand new post from the python dictionary 
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


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    #when id is not correct
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    #find the index
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} does not exist")
    #converting to a python dictionary 
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return{"data": post_dict}
