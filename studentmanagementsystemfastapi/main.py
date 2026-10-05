from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field
from typing import Optional


app=FastAPI(
    title="Student Management API",
    description="Student Management system using FastAPI",
    Version ="1.0.0"
)


class CreateStudent(BaseModel):
    
    name:str=Field(...,min_length=3)
    email_id:str=Field(...,min_length=3)
    age:int=Field(...,gt=0)

class UpdateStudent(BaseModel):
    
    name:Optional[str]=Field(default=None,min_length=3)
    email_id:Optional[str]=Field(default=None,min_length=3)
    age:Optional[int]=Field(default=None,gt=0)

students=[]
next_student_id=1

@app.post("/students",status_code=status.HTTP_201_CREATED)
def create_student(student:CreateStudent):
    global next_student_id
    new_student={
        "id":next_student_id,
        "name":student.name,
        "email_id":student.email_id,
        "age":student.age
    }
    students.append(new_student)
    next_student_id+=1
    return new_student

@app.get("/students")
def get_students():
    return students


@app.get("/students/{id}")
def get_student(id:int):
    for student in students:
        if student["id"]==id:
            return student
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.put("/students/{id}")
def replace_student(id:int , student_update:UpdateStudent):
    for index,student in enumerate(students):
        if student["id"]==id:
            replace_student={
                "id":id,
                "name":student_update.name,
                "email_id":student_update.email_id,
                "age":student_update.age
            }
            students[index]=replace_student
            return replace_student
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )



@app.patch("/students/{id}")
def update_student(id:int , student_update:UpdateStudent):
    for student in students:
        if student["id"]==id:
            update_student=student_update.model_dump(exclude_unset=True)
            student.update(update_student)
            return student
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.delete("/students/{id}")
def delete_student(id:int):
    for index,student in enumerate(students):
        if student["id"]==id:
            deleted_student=students.pop(index)
            return {
                "message":"student deleted successfully",
                "student":deleted_student
            }
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


