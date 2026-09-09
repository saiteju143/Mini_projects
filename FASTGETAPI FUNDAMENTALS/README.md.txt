# Super30 FastAPI GET API Task

## Project Objective

The objective of this project is to create a FastAPI application containing multiple **GET APIs**.

This project helps understand:

* FastAPI application creation
* Installing FastAPI
* Installing Uvicorn
* Creating API routes using `@app.get()`
* Static routes
* Dynamic URL parameters
* Path parameters
* Type hints
* Returning Python dictionaries as JSON responses
* Running FastAPI locally
* Testing API endpoints
* FastAPI Swagger documentation
* FastAPI ReDoc documentation

---

## Project Structure

```text
super30-fastapi-get-api-task/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* REST API
* JSON

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/super30-fastapi-get-api-task.git
```

### 2. Open the project folder

```bash
cd super30-fastapi-get-api-task
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

---

## Requirements

The `requirements.txt` file contains:

```text
fastapi
uvicorn
```

---

## How to Run the Application

Run the following command in the terminal:

```bash
uvicorn main:app --reload
```

The application will normally run at:

```text
http://127.0.0.1:8000
```

---

# API Endpoints

## 1. Home API

### Endpoint

```text
GET /
```

### URL

```text
http://127.0.0.1:8000/
```

### Response

```json
{
    "message": "Welcome to Super30 FastAPI"
}
```

---

## 2. Student API

### Endpoint

```text
GET /student
```

### URL

```text
http://127.0.0.1:8000/student
```

### Response

```json
{
    "name": "Teju",
    "batch": "Super30",
    "role": "Student"
}
```

---

## 3. Course API

### Endpoint

```text
GET /course
```

### URL

```text
http://127.0.0.1:8000/course
```

### Response

```json
{
    "course_name": "Backend Development with FastAPI",
    "mentor": "Super30 Mentor",
    "duration": "8 Weeks",
    "topics": [
        "Python",
        "FastAPI",
        "REST API",
        "Database",
        "Deployment"
    ]
}
```

---

## 4. Skills API

### Endpoint

```text
GET /skills
```

### URL

```text
http://127.0.0.1:8000/skills
```

### Response

```json
{
    "skills": [
        "Python",
        "FastAPI",
        "SQL",
        "Docker",
        "AWS"
    ]
}
```

---

## 5. Addition API

### Endpoint

```text
GET /add/{num1}/{num2}
```

### Example

```text
http://127.0.0.1:8000/add/10/20
```

### Response

```json
{
    "result": 30
}
```

### Another Example

```text
http://127.0.0.1:8000/add/50/25
```

Response:

```json
{
    "result": 75
}
```

The values are supplied dynamically through the URL.

---

## 6. Multiplication API

### Endpoint

```text
GET /multiply/{num1}/{num2}
```

### Example

```text
http://127.0.0.1:8000/multiply/5/8
```

### Response

```json
{
    "result": 40
}
```

---

## 7. Square API

### Endpoint

```text
GET /square/{number}
```

### Example

```text
http://127.0.0.1:8000/square/9
```

### Response

```json
{
    "number": 9,
    "square": 81
}
```

The number is supplied dynamically through the URL.

---

## 8. Even/Odd API

### Endpoint

```text
GET /check/{number}
```

### Example

```text
http://127.0.0.1:8000/check/17
```

### Response

```json
{
    "number": 17,
    "type": "odd"
}
```

### Another Example

```text
http://127.0.0.1:8000/check/20
```

Response:

```json
{
    "number": 20,
    "type": "even"
}
```

---

## 9. Age API

### Endpoint

```text
GET /age/{age}
```

### Example

```text
http://127.0.0.1:8000/age/25
```

### Response

```json
{
    "age": 25,
    "message": "You are an adult."
}
```

The response message changes based on the supplied age.

Possible categories:

* Child
* Teenager
* Adult
* Senior citizen

---

## 10. Table API

### Endpoint

```text
GET /table/{number}
```

### Example

```text
http://127.0.0.1:8000/table/7
```

### Response

```json
{
    "number": 7,
    "table": [
        "7 x 1 = 7",
        "7 x 2 = 14",
        "7 x 3 = 21",
        "7 x 4 = 28",
        "7 x 5 = 35",
        "7 x 6 = 42",
        "7 x 7 = 49",
        "7 x 8 = 56",
        "7 x 9 = 63",
        "7 x 10 = 70"
    ]
}
```

The table number is supplied dynamically through the URL.

---

## 11. Profile API

### Endpoint

```text
GET /profile/{name}/{age}
```

### Example

```text
http://127.0.0.1:8000/profile/Teju/33
```

### Response

```json
{
    "name": "Teju",
    "age": 33
}
```

Both the name and age are dynamic path parameters.

---

## 12. Number Analysis API

### Endpoint

```text
GET /number/{number}
```

### Example

```text
http://127.0.0.1:8000/number/25
```

### Response

```json
{
    "number": 25,
    "square": 625,
    "cube": 15625,
    "even": false
}
```

### Another Example

```text
http://127.0.0.1:8000/number/10
```

Response:

```json
{
    "number": 10,
    "square": 100,
    "cube": 1000,
    "even": true
}
```

---

# Swagger Documentation

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

1. View all available API endpoints.
2. Select a GET endpoint.
3. Click **Try it out**.
4. Enter dynamic values.
5. Click **Execute**.
6. View the JSON response.

---

# ReDoc Documentation

FastAPI also automatically provides ReDoc documentation.

Open:

```text
http://127.0.0.1:8000/redoc
```

ReDoc provides a clean documentation view of the API endpoints.

---

# Testing the APIs

The APIs can be tested using:

* Browser
* Swagger UI
* Postman
* Thunder Client
* curl

For example:

```text
http://127.0.0.1:8000/add/50/25
```

should return:

```json
{
    "result": 75
}
```

---

# Dynamic Path Parameters

Several APIs in this project use dynamic path parameters.

For example:

```python
@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    return {"result": num1 + num2}
```

When we call:

```text
/add/10/20
```

FastAPI automatically passes:

```text
num1 = 10
num2 = 20
```

The API then returns:

```json
{
    "result": 30
}
```

This demonstrates how dynamic URL parameters work in FastAPI.

---

# GET APIs Only

This project implements **GET APIs only**.

The following HTTP methods are not used:

* POST
* PUT
* PATCH
* DELETE

---

# YouTube Demonstration

The project demonstration video should show:

* Project folder
* `main.py`
* FastAPI application
* Uvicorn server running
* API endpoints
* Dynamic API endpoints
* At least 8 GET endpoints executed live
* One API tested with different dynamic values
* Swagger `/docs`
* JSON responses
* Brief explanation of the code

---

# Learning Outcome

After completing this project, I understand:

* How to create a FastAPI application
* How `FastAPI()` works
* How `@app.get()` creates GET endpoints
* How route functions work
* How static routes work
* How dynamic routes work
* How path parameters work
* How Python type hints are used with FastAPI
* How Python dictionaries are returned as JSON
* How to run an API using Uvicorn
* How to test APIs
* How FastAPI generates Swagger and ReDoc documentation

---

# Author

**Student Name:** Teju

**Batch:** Super30

**Project:** Super30 FastAPI GET API Task
