from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
class coordIn(BaseModel):
    password : str
    lat: float
    long: float
    zoom: Optional[int]

class coordOut(BaseModel):
    lat: float
    long: float
    zoom: Optional[int]

#get
@app.get('/')
def helloword():
    return {'message': 'Hello, World!'}

# post

@app.post('/coordonee/',response_model=coordOut)
async def position(coord : coordIn):
    return coord

# put

# @app.get ('/components/')
# async def read_components(number: int,text: Optional [str]):
#     return {'number': number, 'text': text}