from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    email: str
    
class StudentRespose(BaseModel):
    name: str
    age: int

class Employee(BaseModel):
    name: str
    salary: int
    department: str
    
class EmployeeResponse(BaseModel):
    name: str
    department: str

@app.post('/student', response_model=StudentRespose)
def add_student(student: Student):
    return student

@app.post("/employee", status_code=status.HTTP_201_CREATED, response_model=EmployeeResponse)
def add_employee(employee: Employee):
    return employee