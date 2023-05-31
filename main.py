from fastapi import FastAPI
import database 
import models
app=FastAPI()
@app.get('/')
def index():
    return "This is HomePage"

# create task operation
@app.post('/task')
def create(data:models.Task):
    database.create_task(data)
    return "task added"


#read all tasks
@app.get('/task')
def readAll():
    tasks=database.read_all()
    return {"Tasks":tasks}


#read specific task
@app.get('/task/{id}')
def readOne(id:int):
    task=database.read_one(id)
    return {"Task":task}


# update task
@app.put('/task/{id}')
def update(id:int,data: models.Task):
    database.update(id,data)
    return f"the data of id {id} is updated"

# delete task
@app.delete('/task/{id}')
def deleteTask(id:int):
    database.delete(id)
    return f"the task of id {id} is deleted"