from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field
from database import get_connection
from typing import Optional,Literal


app=FastAPI(
    title="Task Management API",
    description="Task management API using FastAPI + Neon Postgresql",
    version="A"
)

class CreateProject(BaseModel):
    
    name:str=Field(...,min_length=3)
    description:Optional[str]=Field(default=None,min_length=3)

class CreateTask(BaseModel):
    title:str=Field(...,min_length=3)
    description:Optional[str]=Field(default=None,min_length=3)
    project_id:int=Field(...,gt=0)

class AssignTask(BaseModel):
    assigned_to:str=Field(...,min_length=3)

class UpdateTaskStatus(BaseModel):
    status:Literal[
        "pending",
        "In_progress",
        "Completed"
    ]

@app.post("/projects" , status_code=status.HTTP_201_CREATED)
def create_project(project:CreateProject):
    connection=get_connection()
    cursor=connection.cursor()
    try:
        cursor.execute("""
        INSERT INTO projects
        (name,description)
        VALUES (%s,%s)
        RETURNING id,name,description,created_at;
        """,(project.name,project.description))
        new_project=cursor.fetchone()
        connection.commit()
        return {
            "id":new_project[0],
            "name":new_project[1],
            "description":new_project[2],
            "created_at":new_project[3]
        }
    except Exception as e:
        connection.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    finally:
        cursor.close()
        connection.close()
    

@app.post("/tasks",status_code=status.HTTP_201_CREATED)
def create_tasks(task:CreateTask):
    connection=get_connection()
    cursor=connection.cursor()
    try:
        cursor.execute("""
        INSERT INTO tasks
        (title,description,project_id)
        VALUES (%s,%s,%s)
        RETURNING id,title,description,project_id,assigned_to,status,created_at;
        """,(task.title,task.description,task.project_id))
        new_task=cursor.fetchone()
        connection.commit()
        return {
            "id":new_task[0],
            "title":new_task[1],
            "description":new_task[2],
            "project_id":new_task[3],
            "assigned_to":new_task[4],
            "status":new_task[5],
            "created_at":new_task[6]      
        }
    except Exception as e:
        connection.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    finally:
        cursor.close()
        connection.close()

@app.put("/tasks/{task_id}/assign")
def assign_task(task_id:int , assign:AssignTask):
    connection=get_connection()
    cursor=connection.cursor()
    
    cursor.execute("""
    UPDATE tasks
    SET assigned_to =%s
    WHERE id=%s
    RETURNING id,title,description,project_id,assigned_to,status,created_at;
    """,(assign.assigned_to,task_id))
    updated_task=cursor.fetchone()
    if updated_task is None:
        connection.rollback()
        cursor.close()
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    connection.commit()
    return {
            "id":updated_task[0],
            "title":updated_task[1],
            "description":updated_task[2],
            "project_id":updated_task[3],
            "assigned_to":updated_task[4],
            "status":updated_task[5],
            "created_at":updated_task[6]      
        }

@app.put("/tasks/{task_id}/status")
def update_status(task_id:int,status:UpdateTaskStatus):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute("""
    UPDATE tasks
    SET status=%s
    WHERE id=%s
    RETURNING id,title,description,project_id,assigned_to,status,created_at;
    """,(status.status,task_id))
    update_status=cursor.fetchone()
    if update_status is None:
        connection.rollback()
        cursor.close()
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    connection.commit
    return {
        "id":update_status[0],
        "title":update_status[1],
        "description":update_status[2],
        "project_id":update_status[3],
        "assigned_to":update_status[4],
        "status":update_status[5],
        "created_at":update_status[6]      
        }

@app.get("/tasks")
def get_tasks():
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute("""
    SELECT * FROM tasks 
    ORDER BY id;
    """)
    rows=cursor.fetchall()
    cursor.close()
    connection.close()
    tasks=[]
    for row in rows:
        tasks.append({
        "id":row[0],
        "title":row[1],
        "description":row[2],
        "project_id":row[3],
        "assigned_to":row[4],
        "status":row[5],
        "created_at":row[6]      
        })
    return tasks

@app.get("/tasks/filters")
def filter_tasks(
    project_id:int|None=None,
    assigned_to:str|None=None,
    status:str|None=None   
):
    connection=get_connection()
    cursor=connection.cursor()
    query="""
    SELECT * FROM tasks
    WHERE 1=1 
    """
    parameters=[]
    if project_id:
        query +=" AND project_id=%s"
        parameters.append(project_id)
    if assigned_to:
        query +=" AND assigned_to=%s"
        parameters.append(assigned_to)
    if status:
        query +=" AND status=%s"
        parameters.append(status)

    query +=" ORDER BY id"
    cursor.execute(query,parameters)
    rows=cursor.fetchall()
    cursor.close()
    connection.close()
    tasks=[]
    for row in rows:
        tasks.append({
        "id":row[0],
        "title":row[1],
        "description":row[2],
        "project_id":row[3],
        "assigned_to":row[4],
        "status":row[5],
        "created_at":row[6]      
        })
    return tasks

@app.delete("/tasks/{task_id}")
def delete_tasks(task_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute("""
    DELETE FROM tasks
    WHERE id=%s
    RETURNING id;
""",(task_id,))
    deleted_task=cursor.fetchone()
    if deleted_task is None:
        connection.rollback()
        cursor.close()
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"

        )
    connection.commit()
    return {
        "Message":"Task deleted successfully",
        "Deleted_task":deleted_task[0]
    
    }









