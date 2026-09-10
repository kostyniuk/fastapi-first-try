from fastapi import FastAPI
from pydantic import BaseModel

class Post(BaseModel):
    author: str
    text: str
    is_public: bool | None = True

app = FastAPI()

@app.get('/')
def read_root():
    return 'Hello FastAPI'

@app.get('/posts/{id}/info/{infoId}')
def read_post(id: int, infoId: int, queryA: str | None = None):
    return f"Post {id}, info {infoId}, q: {str(queryA)}"

@app.post('/posts')
def create_post(post: Post):
    return post