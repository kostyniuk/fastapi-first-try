from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return 'Hello FastAPI'

@app.get('/test')
def read_test():
    return 'Some test GET route'

@app.get('/posts/{id}/info/{infoId}')
def read_post(id: int, infoId: int, queryA: str | None = None):
    return f"Post {id}, info {infoId}, q: {str(queryA)}"