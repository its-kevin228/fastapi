from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title='todo_app', version="v1.0")

class Todo(BaseModel):
    name:str
    description: str
    due_date:str

store_task = [

]

@app.get('/todo/{id}')
async def get_id():
    try:
        return store_task[id]
    except:
        raise HTTPException(status_code = 404, detail='Task not found in database')

@app.get('/todos',response_model= list[Todo])
async def get_todos():
    return store_task

@app.get('/')
async def welcome():
    return {'message': 'Welcome to the TODO API'}

@app.post('/todo')
async def ajoutertodo(todo: Todo):
    store_task.append(todo)
    return todo

@app.put('/todo/{id}')
async def update(id: int, new_todo: Todo):
    try:
        store_task[id] = new_todo
        return store_task[id]
    except:
        raise HTTPException(status_code = 404, detail='Task not found in database')
    

@app.delete('/todo/{id}')
async def delete_task(id: int):
    try:
        obj = store_task[id]
        store_task.pop(id)
        return obj
    except:
        raise HTTPException(status_code = 404, detail='Task not found in database')