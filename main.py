from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class coord(BaseModel):
    lat: float
    long: float
    zoom: Optional[int]

#get
@app.get('/')
def helloword():
    return {'message': 'Hello, World!'}

# post

@app.post('/coordonee/{propo}')
async def position(propo:int,coord : coord):
    return {'propo':propo,'location': coord.dic()}

# put

# @app.get ('/components/')
# async def read_components(number: int,text: Optional [str]):
#     return {'number': number, 'text': text}