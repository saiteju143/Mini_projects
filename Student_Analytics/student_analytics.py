from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import numpy as np
import plotly.graph_objects as go



app=FastAPI()

students = [
    {"student_id": 1, "name": "Rahul", "python": 85, "mathematics": 78, "data_science": 88},
    {"student_id": 2, "name": "Priya", "python": 92, "mathematics": 89, "data_science": 95},
    {"student_id": 3, "name": "Arjun", "python": 76, "mathematics": 82, "data_science": 79},
    {"student_id": 4, "name": "Sneha", "python": 88, "mathematics": 91, "data_science": 86},
    {"student_id": 5, "name": "Kiran", "python": 69, "mathematics": 74, "data_science": 72},
    {"student_id": 6, "name": "Anjali", "python": 95, "mathematics": 93, "data_science": 97},
    {"student_id": 7, "name": "Ravi", "python": 81, "mathematics": 77, "data_science": 84},
    {"student_id": 8, "name": "Divya", "python": 87, "mathematics": 85, "data_science": 90},
    {"student_id": 9, "name": "Suresh", "python": 73, "mathematics": 68, "data_science": 75},
    {"student_id": 10, "name": "Neha", "python": 90, "mathematics": 88, "data_science": 92},
    {"student_id": 11, "name": "Akash", "python": 79, "mathematics": 83, "data_science": 81},
    {"student_id": 12, "name": "Pooja", "python": 84, "mathematics": 79, "data_science": 87},
    {"student_id": 13, "name": "Varun", "python": 91, "mathematics": 86, "data_science": 89},
    {"student_id": 14, "name": "Lakshmi", "python": 72, "mathematics": 76, "data_science": 70},
    {"student_id": 15, "name": "Rohit", "python": 86, "mathematics": 90, "data_science": 85},
    {"student_id": 16, "name": "Kavya", "python": 94, "mathematics": 96, "data_science": 93},
    {"student_id": 17, "name": "Manoj", "python": 68, "mathematics": 71, "data_science": 74},
    {"student_id": 18, "name": "Aishwarya", "python": 89, "mathematics": 87, "data_science": 91},
    {"student_id": 19, "name": "Sanjay", "python": 77, "mathematics": 80, "data_science": 78},
    {"student_id": 20, "name": "Meena", "python": 93, "mathematics": 92, "data_science": 96}
]


#all students
@app.get("/students")
def display_students():
    return {"Students":students}

#Student Details
@app.get("/student/{student_id}")
def student_details(student_id:int):
    for student in students:
        if student["student_id"]==student_id:
            return student
        
    return {"message":"Student not found"}

#python_average
@app.get("/average/python")
def python_average():
    python=[]
    for student in students:
        python.append(student["python"])
    avg=np.mean(python)
    return{
        "Python_Average":avg
    }

#mathematics_average
@app.get("/average/mathematics")
def mathematics_average():
    mathematics=[]
    for student in students:
        mathematics.append(student["mathematics"])
    avg=np.mean(mathematics)
    return{
        "Mathematics_Average":avg
    }     

#Data Science_average
@app.get("/average/data-science")
def data_science():
    data_science=[]
    for student in students:
        data_science.append(student["data_science"])
    avg=np.mean(data_science)
    return{
        "data_science_Average":avg
    } 

#topper
@app.get("/topper")
def topper():
    mean_details=[]
    for student in students:
        marks=[student["python"],student["mathematics"],student["data_science"]]
        avg=np.mean(marks)
        mean_details.append({"Name":student["name"] , "Average": avg})
    max_avg=0
    topper_student=""
    for student in mean_details:
        if student["Average"]>max_avg:
            max_avg=student["Average"]
            topper_student=student["Name"]
    return{
        "Topper_student":topper_student
    }

#passed
@app.get("/passed")
def passed():
    passed_students=[]
    for student in students:
        marks=[student["python"],student["mathematics"],student["data_science"]]
        Total=np.sum(marks)
        percentage=(Total/300)*100
        if percentage>=45:
            passed_students.append(student)
            
    return{"Passed_Students":passed_students}


#failed
@app.get("/failed")
def failed():
    failed_students=[]
    for student in students:
        marks=[student["python"],student["mathematics"],student["data_science"]]
        Total=np.sum(marks)
        percentage=(Total/300)*100
        if percentage<45:
            failed_students.append(student)
            
    return{"Failed_Students":failed_students}

#statistics
@app.get("/statistics")
def statistics():

    python_marks = []
    mathematics_marks = []
    data_science_marks = []

    for student in students:
        python_marks.append(student["python"])
        mathematics_marks.append(student["mathematics"])
        data_science_marks.append(student["data_science"])

    # Subject averages
    python_average = float(np.mean(python_marks))
    mathematics_average = float(np.mean(mathematics_marks))
    data_science_average = float(np.mean(data_science_marks))

    # Highest marks
    python_highest = int(np.max(python_marks))
    mathematics_highest = int(np.max(mathematics_marks))
    data_science_highest = int(np.max(data_science_marks))

    # Lowest marks
    python_lowest = int(np.min(python_marks))
    mathematics_lowest = int(np.min(mathematics_marks))
    data_science_lowest = int(np.min(data_science_marks))

    # Overall average
    all_marks = python_marks + mathematics_marks + data_science_marks
    overall_average = float(np.mean(all_marks))

    return {
        "Subject_Averages": {
            "Python": python_average,
            "Mathematics": mathematics_average,
            "Data_Science": data_science_average
        },

        "Highest_Marks": {
            "Python": python_highest,
            "Mathematics": mathematics_highest,
            "Data_Science": data_science_highest
        },

        "Lowest_Marks": {
            "Python": python_lowest,
            "Mathematics": mathematics_lowest,
            "Data_Science": data_science_lowest
        },

        "Overall_Average": overall_average
    }

#plotly_visualization
@app.get("/visualization",response_class=HTMLResponse)

def visualization():
    python_marks = []
    mathematics_marks = []
    data_science_marks = []

    for student in students:
        python_marks.append(student["python"])
        mathematics_marks.append(student["mathematics"])
        data_science_marks.append(student["data_science"])

    subjects = ["Python", "Mathematics", "Data Science"]

    averages = [
        np.mean(python_marks),
        np.mean(mathematics_marks),
        np.mean(data_science_marks)
    ]


    fig=go.Figure(
        data=[
            go.Bar(
                x=subjects,
                y=averages
            )
        ]
    )

    fig.update_layout(
        title="Average Marks Across Subjects",
        xaxis_title="Subjects",
        yaxis_title="Average Marks")

    return fig.to_html(full_html=True)


#studentcomparison
@app.get("/studentcomparison" , response_class=HTMLResponse)
def student_comparison():
    student_averages=[]
    for student in students:
        marks=[student["python"],
               student["mathematics"],
               student["data_science"]]
        average=np.mean(marks)
        student_averages.append({"Name":student["name"],"Average":average})

    student_averages.sort(
        key=lambda student:student["Average"],
        reverse=True
    )
    top_5_students=student_averages[:5]

    top_names=[]
    top_averages=[]

    for student in top_5_students:
        top_names.append(student["Name"])
        top_averages.append(student["Average"])


    fig=go.Figure()
    fig.add_trace(go.Bar(
        x=top_names,
        y=top_averages
    ))
    fig.update_layout(
        title="Top 5 Students",
        xaxis_title="Student_Names",
        yaxis_title="Top_5_Averages"
    )
    return fig.to_html(full_html=True)


     

        

    
        