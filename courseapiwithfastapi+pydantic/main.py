from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Optional


app=FastAPI(
    title="Courses Management",
    description="Backend Management of courses using API",
    version="1.0.0"
)

class CourseCreate(BaseModel):
    title:str = Field(
        ...,
        min_length=3)
    description:str=Field(
        ...,
        min_length=3)
    price:float=Field(
        ...,
        gt=0)
    duration:int=Field(
        ...,
        gt=0)
    instructor:str=Field(
        ...,
        min_length=2)
    category:str=Field(
        ...,
        min_length=2)
    rating:float=Field(
        ...,
        gt=0,
        le=5)
    active:bool

class CourseUpdate(BaseModel):
    title:Optional[str] = Field(
        default=None,
        min_length=3)
    description:Optional[str]=Field(
        default=None,
        min_length=3)
    price:Optional[float]=Field(
        default=None,
        gt=0)
    duration:Optional[int]=Field(
        default=None,
        gt=0)
    instructor:Optional[str]=Field(
        default=None,
        min_length=2)
    category:Optional[str]=Field(
        default=None,
        min_length=2)
    rating:Optional[float]=Field(
        default=None,
        gt=0,
        le=5)
    active:Optional[bool]=None

class CourseResponse(BaseModel):
    id:int
    title:str
    description:str
    price:float
    duration:int
    instructor:str
    category:str
    rating:float
    active:bool



courses=[]
next_course_id=1

@app.post("/courses",response_model=CourseResponse)
def create_course(course:CourseCreate):
    global next_course_id
    new_course={
        "id":next_course_id,
        "title":course.title,
        "description":course.description,
        "price": course.price,
        "duration": course.duration,
        "instructor": course.instructor,
        "category": course.category,
        "rating": course.rating,
        "active": course.active
    }
    courses.append(new_course)
    next_course_id+=1
    return new_course



@app.get("/courses" , response_model=list[CourseResponse])
def get_course(
    category:Optional[str]=None,
    max_price:Optional[float]=None,
    min_price:Optional[float]=None,
    active:Optional[bool]=None):

    filtered_courses=courses
    if category is not None:
        filtered_courses=[
            course
            for course in filtered_courses
            if course["category"].lower()==category.lower()
            ]
    if max_price is not None:
        filtered_courses=[
            course
            for course in filtered_courses
            if course["price"]<=max_price
        ]
    if min_price is not None:
            filtered_courses=[
            course
            for course in filtered_courses
            if course["price"]>=min_price
        ]
    if active is not None:
         filtered_courses=[
            course
            for course in filtered_courses
            if course["active"]==active
              
        ]
    return filtered_courses

@app.put("/courses/{course_id}" , response_model=CourseResponse)
def update_course(course_id:int,course_update:CourseUpdate):
    for course in courses:
        if course["id"]==course_id:
            update_data=course_update.model_dump(exclude_unset=True)
            course.update(update_data)
            return course
    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )
     

    
    



