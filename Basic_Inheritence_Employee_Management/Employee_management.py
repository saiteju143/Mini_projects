
class Employee:
    def __init__(self,employee_id,name,salary,department):
        self.employee_id=employee_id
        self.name=name
        self.salary=salary
        self.department=department
    def display_details(self):
        print("Employee_id:" , self.employee_id)
        print("Name:" , self.name)
        print("Department:" , self.department)
    def calculate_salary(self):
        return self.salary
        

class Developer(Employee):
    def __init__(self,employee_id,name,salary,department,programming_lang):
        super().__init__(employee_id,name,salary,department)
        self.programming_lang=programming_lang
class Manager(Employee):
    def __init__(self,employee_id,name,salary,department,team_size):
        super().__init__(employee_id,name,salary,department)
        self.team_size=team_size

class Hr(Employee):
    def __init__(self,employee_id,name,salary,department,region):
        super().__init__(employee_id,name,salary,department)
        self.region=region

# Developer objects
developer1 = Developer("1001", "Saikumar", 300000, "IT", "Python")
developer2 = Developer("1002", "Rahul", 350000, "IT", "Java")


# Manager objects
manager1 = Manager("1005", "Premkumar", 600000, "IT", 45)
manager2 = Manager("1006", "Arjun", 550000, "Operations", 30)


# HR objects
hr1 = Hr("1007", "Prema", 60000, "HR", "Hyderabad")
hr2 = Hr("1008", "Ananya", 70000, "HR", "Bangalore")

print(developer1.programming_lang)
print(manager1.team_size)
print(hr1.region)


developer1.display_details()
print("Programming_lang:" , developer1.programming_lang)
print("Salary:", developer1.calculate_salary())

manager1.display_details()
print("Team_size:" , manager1.team_size)
print("Salary:", manager1.calculate_salary())

hr1.display_details()
print("Region:" , hr1.region)
print("Salary:", hr1.calculate_salary())