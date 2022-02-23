
from distutils.log import error
from operator import index
from turtle import pos
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from . import models
from .database import  engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

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

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return{"status ": "seccess"}

#Post method
@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM "Socialmedia_posts" """)
    posts = cursor.fetchall()
    return{"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):   
    #preventing sqli and also validating user input
    cursor.execute(""" INSERT INTO socialmedia_posts (title, content) VALUES (%s, %s) RETURNING * """, (post.title, post.content))
    new_post = cursor.fetchone
    conn.commit()
    return{"data": new_post}

#calling a particular post id 
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    cursor.execute(""" SELECT * FROM socialmedia_posts WHERE id = %s """, (str(id)))
    post = cursor.fetchone()
    if not post :
        #error handling 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"post with id: {id} was not found ")
    return{"post_details": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    cursor.execute(""" DELETE FROM socialmedia_posts WHERE ID = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()

    conn.commit()
    #when id is not correct
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} does not exist")
   
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(""" UPDATE socialmedia_posts SET title= %s, content = %s WHERE id = %s RETURNING * """, (post.title, post.content, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    #find the index
    
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} does not exist")
    
    return{"data": updated_post}
