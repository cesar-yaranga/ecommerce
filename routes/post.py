from fastapi import APIRouter

from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

post = APIRouter()

posts = []

#Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

@post.get('/posts')
def get_posts():
    return posts

@post.post('/posts')
def save_posts(post: Post):
    post.id = uuid()
    posts.append(post.dict())
    return "receive"

@post.get('/post/{post_id}')
def get_posts():
    return "received"