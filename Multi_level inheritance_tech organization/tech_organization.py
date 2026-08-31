
class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def person_details(self):
        print("Name:", self.name)
        print("Age:",self.age)
        print("City:" , self.city)
    
        

class Employee(Person):
    def __init__(self,name,age,city,Employee_id,salary,company):
        super().__init__(name,age,city)
        self.Employee_id=Employee_id
        self.salary=salary
        self.company=company
    def employee_details(self):
        print("Employee_id:", self.Employee_id)
        print("Salary:",self.salary)
        print("Company:" , self.company)
        
        
        
class Developer(Employee):
    def __init__(self,name,age,city,Employee_id,salary,company,language,framework,experience):
        super().__init__(name,age,city,Employee_id,salary,company)
        self.language=language
        self.framework=framework
        self.experience=experience
    def developer_details(self):
        print("language:",self.language)
        print("Framework:",self.framework)
        print("Experience:" ,self.experience)


dev1 = Developer("Teju", 33, "Hyderabad", "E101", 80000,
                 "ABC", "Python", "Django", 4)

dev2 = Developer("Rahul", 28, "Bangalore", "E102", 70000,
                 "XYZ", "Java", "Spring", 3)

dev3 = Developer("Priya", 30, "Chennai", "E103", 75000,
                 "PQR", "Python", "Flask", 5)

dev4 = Developer("Arjun", 27, "Delhi", "E104", 65000,
                 "LMN", "JavaScript", "React", 2)

dev5 = Developer("Ananya", 31, "Pune", "E105", 90000,
                 "DEF", "Python", "FastAPI", 6)


dev1.person_details()
dev3.employee_details()
dev5.developer_details()