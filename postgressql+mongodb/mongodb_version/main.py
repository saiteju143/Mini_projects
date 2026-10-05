from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field
from database import project_collection,task_collection
from bson import ObjectId
from typing import Optional,Literal

app=FastAPI(
    title="Project Management API",
    description="Project Management API using FastAPI + MongoDB ",
    Version="B"
)

class CreateProject(BaseModel):
    name:str=Field(...,min_length=3)
    description:str | None=None
class CreateTask(BaseModel):
    title:str=Field(...,min_length=3)
    description:str | None=None
    project_id:str
class AssignTask(BaseModel):
    assigned_to:str=Field(...,min_length=3)
class UpdateStatus(BaseModel):
    status: Literal[
        "pending",
        "in_progress",
        "completed"
    ]

    


@app.post("/projects", status_code=201)
def create_project(project: CreateProject):

    project_data = {
        "name": project.name,
        "description": project.description
    }

    result = project_collection.insert_one(project_data)

    return {
        "id": str(result.inserted_id),
        "name":project.name,
        "description":project.description
    }


@app.post("/tasks",status_code=201)
def create_task(task:CreateTask):
    task_data={
        "title":task.title,
        "description":task.description,
        "project_id":task.project_id,
        "assigned_to":None,
        "status":"Pending"
    }
    result=task_collection.insert_one(task_data)
    return{
        "id":str(result.inserted_id),
        "title":task.title,
        "description":task.description,
        "project_id":task.project_id,
        "assigned_to":None,
        "status":"Pending"
    }

@app.put("/assign/{task_id}")
def assign_task(task_id:str,assign:AssignTask):
    result=task_collection.update_one(
        {
            "_id":ObjectId(task_id)
    },
    {
        "$set":{
            "assigned_to":assign.assigned_to
        }
    }

    )
    if result.matched_count==0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return {
       "message": "Task assigned successfully"
    }

@app.put("/update_status/{task_id}")
def update_status(task_id:str,status:UpdateStatus):
    result=task_collection.update_one({
        "_id":ObjectId(task_id)
    },
    {
        "$set":{
            "status":status.status
        }
    }
    )
    if result.matched_count==0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"

        )
    return{
        "message":"Task status updated successfully"
    }

@app.get("/retrieve_tasks")
def retrieve_tasks():
    tasks=list(task_collection.find())
    for task in tasks:
        task["id"]=str(task["_id"])
        del task["_id"]
    return tasks

@app.get("/filtering_tasks")
def filter_tasks(
    status:str |None=None,
    project_id:str|None=None,
    assigned_to:str|None=None
):
    filters={}
    if status:
        filters["status"]=status
    if project_id:
        filters["project_id"]=project_id
    if assigned_to:
        filters["assigned_to"]=assigned_to
    tasks=list(task_collection.find(filters))
    for task in tasks:
        task["id"]=str(task["_id"])
        del task["_id"]
    return tasks

@app.delete("/deletetasks/{task_id}")
def delete_tasks(task_id:str):
    result=task_collection.delete_one(
        {
            "_id":ObjectId(task_id)
        }
    )
    if result.deleted_count==0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return{
        "message":"Task deleted successfully"
    }