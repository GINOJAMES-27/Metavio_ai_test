from fastapi import FastAPI
#from model import Task




app=FastAPI()

Task=[{"id": 1,
    "title":"Task 1",
    "description":"First task",
    "status":"pending",
    "priority":"high",
    "created_at":"2024-06-01",
    "updated_at":"2024-06-01"
    },{"id": 2,
    "title":"Task 2",
    "description":"Second task",
    "status":"in progress",
    "priority":"medium",
    "created_at":"2024-06-01",
    "updated_at":"2024-06-01"},
    {"id": 3,
    "title":"Task 3",
    "description":"third task",
    "status":"in progress",
    "priority":"medium",
    "created_at":"2024-06-01",
    "updated_at":"2024-06-01"},]


#To check if the API is working
@app.get("/")
def Hello():
    return {"message": "Hello, World!"}

#list all tasks
@app.get("/tasks")
def get_tasks():
    return {"tasks": [Task]}
#get a single task by id
@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    for  i in Task:
        if i["id"]==task_id:
            return {task_id:i}
        
    return {"message":"Task not found"}
#create a new task
@app.post("/tasks")
def create(task:dict):
    Task.append(task)
    return {"message":"Task created successfully"}

#Delete a task by id
@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    for i in Task:
        if i["id"] == task_id:
            Task.remove(i)
            return {"message": "Task deleted successfully"}
    return {"message": "Task not found"}

@app.put("/tasks/{task_id}")

#update a task by id
def update_task(task_id:int, updated_task:dict):  
    for i in Task:
        if i["id"] == task_id:
            i.update(updated_task)
            return {"message": "Task updated successfully"}
    return {"message": "Task not found"}










