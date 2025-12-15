class Person:
    def __init__(self,name,gender,age):
        self.ename = name 
        self.egender = gender 
        self.eage = age 
    def __str__(self):
        return f"{self.ename} {self.egender} {self.eage}"
class Employee(Person):
    def __init__(self,name,gender,age,salary):
        Person.__init__(self,name,gender,age)
        self.esalary = salary 
    def __str__(self):
        return f"{self.ename} {self.egender} {self.eage} {self.esalary}"

fobj = open("records.txt","r")
employees = []
for line in fobj:
    columns = line.split()
    name = columns[0]
    gender = columns[1]
    age = int(columns[2])
    salary = int(columns[3])
    employee = Employee(name,gender,age,salary)
    employees.append(employee)
for employee in employees:
    print(employee)
