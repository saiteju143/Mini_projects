from fastapi import FastAPI
import numpy as np

app=FastAPI()


#homeAPI
@app.get("/")
def home():
    return{"message": "Welcome to Super30 FastAPI"}

#Student API
@app.get("/student")
def get_student():
    return{
"name": "teju",
"batch": "Super30",
"role": "Student"}

#course API
@app.get("/course")
def get_course():
    return{"course_name": "Backend Development with FastAPI",
           "mentor": "Teju",
           "duration": "8 Weeks",
           "topics": ["Python","FastAPI","REST API","Database","Deployment"]
           }

#skills API
@app.get("/skills")
def get_skills():
    return{"skills": ["python" , "AWS" , "JAVA" , "SQL"]}

#addition API
@app.get("/add/{num1}/{num2}")
def get_add(num1:int,num2:int):
    return {"result":num1+num2}

#multiply API
@app.get("/multiply/{num1}/{num2}")
def get_multiply(num1:int,num2:int):
    return {"result":num1*num2}

#Even/Odd API
@app.get("/check/{num}")
def get_check(num:int):
    if num%2==0:
        type="even"
    else:
        type="odd"

    return {"number":num,
            "type":type}


#Age API
@app.get("/age/{age}")
def get_age(age:int):
    if age < 16:
        message="You are a child."
    elif age < 20:
        message = "You are a teenager."
    elif age < 60:
        message = "You are an adult."
    else:
        message = "You are a senior citizen."
    return {"Age":age,
            "Message":message}

#Table API
@app.get("/table/{num}")
def get_table(num:int):

    table=[]
    for i in range(1,11):
        table.append(f"{num} x {i} ={num*i}")

    return{"Number": num,
           "Table":table}

#Profile API
@app.get("/profile/{name}/{age}")
def get_profile(name:str , age:int):
    return{"name": name,
           "age":age}

#Number Analysis API
@app.get("/number/{num}")
def number_analysis(num:int):
    return{"number": num,
           "square":num**2,
           "cube":num**3,
           "even":num%2==0}

    





           




