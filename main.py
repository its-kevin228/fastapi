from fastapi import FastAPI

app = FastAPI()

#get
@app.get('/')
def helloword():
    return {'message': 'Hello, World!'}