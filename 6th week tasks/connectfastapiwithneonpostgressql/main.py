from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional

from database import get_connection

app=FastAPI(
    title="Student course management API",
)
#test message
@app.get("/")
def home():
    return {
        "message":"Student course management API is running"
    }

class StudentCreate(BaseModel):
    name:str
    email_id:str
class CourseCreate(BaseModel):
    name:str
    description:str
class EnrollmentCreate(BaseModel):
    student_id:int
    course_id:int


@app.post("/students")
def create_student(student:StudentCreate):
    connection=get_connection()
    cursor=connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO students(name,email_id)
            VALUES(%s,%s)
            RETURNING id,name,email_id,created_at;

        """,(student.name,student.email_id))
        new_student=cursor.fetchone()
        connection.commit()
        return{
            "message":"student created successfully",
             "student":{
                "id": new_student[0],
                "name":new_student[1],
                "email_id":new_student[2],
                 "created_at":new_student[3]}
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



@app.post("/courses")
def create_course(course:CourseCreate):
    connection=get_connection()
    cursor=connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO courses(name,description)
            VALUES(%s,%s)
            RETURNING id,name,description,created_at;

        """,(course.name,course.description))
        new_course=cursor.fetchone()
        connection.commit()
        return{
            "message":"Courses created successfully",
             "course":{
                "id":new_course[0],
                "name":new_course[1],
                "description":new_course[2],
                "created_at":new_course[3]      

             }
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
    
@app.post("/enrollments")
def create_enrollment(enrollment:EnrollmentCreate):
    connection=get_connection()
    cursor=connection.cursor()
    try:

        cursor.execute("""
            INSERT INTO enrollments(student_id,course_id)
            VALUES(%s,%s)
            RETURNING id,student_id,course_id,enrolled_at;
        """,(enrollment.student_id,enrollment.course_id))
        new_enrollment=cursor.fetchone()
        connection.commit()
        return{
            "message":"Students enrolled successfully",
            "id":new_enrollment[0],
            "student_id":new_enrollment[1],
            "course_id":new_enrollment[2],
            "enrolled_At":new_enrollment[3],

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


@app.get("/enrollments")
def get_enrollments():
    connection=get_connection()
    cursor=connection.cursor()
    
    cursor.execute("""
        SELECT 
            e.id,
            s.id AS student_id,
            s.name AS student_name,
            s.email_id,
            c.id AS course_id,
            c.name AS course_name,
            e.enrolled_at
        FROM enrollments e
        JOIN students s
            ON e.id=s.id
        JOIN courses c 
            ON e.id=c.id
        ORDER BY e.id;
    """)
    rows=cursor.fetchall()
    cursor.close()
    connection.close()
    enrollments=[]
    for row in rows:
        enrollments.append({
            "enrollment_id":row[0],
            "student_id":row[1],
            "student_name":row[2],
            "email_id":row[3],
            "course_id":row[4],
            "course_name":row[5],
            "enrolled_at":row[6]
        })
    return enrollments

class StudentUpdate(BaseModel):
    name:str
    email_id:str

@app.put("/students/{student_id}")
def update_student(student_id:int,student:StudentUpdate):
    connection=get_connection()
    cursor=connection.cursor()

    try:
        cursor.execute("""
        UPDATE students
            SET
                name=%s,
                email_id=%s
            WHERE id=%s
        RETURNING id,name,email_id,created_at;
        """,(student.name,student.email_id,student_id))
        updated_student=cursor.fetchone()
        if updated_student is None:
            raise HTTPException(
                status_code=404,
                detail="studen not found"
            )
        connection.commit()
        return{
            "message":"student updated successfully",
            "student":{
                "id":updated_student[0],
                "name":updated_student[1],
                "email_id":updated_student[2],
                "created_at":updated_student[3]
            
            }
        }
    except HTTPException:
        connection.rollback()
        raise

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)

        )
    finally:
        cursor.close()
        connection.close()

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    try:
        cursor.execute("""
        DELETE FROM students
        WHERE id=%s
        RETURNING id;
        """,(student_id))
        deleted_student=cursor.fetchone()
        if deleted_student is None:
            raise HTTPException(
                status_code=404,
                detail="student not found"
            )
        connection.commit()
        return{
            "message":"student deleted successfully",
            "student_id":deleted_student[0]
        }
    except HTTPException:
        connection.rollback()
        raise
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    finally:
        cursor.close()
        connection.close()





        