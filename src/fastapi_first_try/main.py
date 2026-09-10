from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return 'Hello FastAPI'

@app.get('/test')
def read_test():
    return 'Some test GET route'