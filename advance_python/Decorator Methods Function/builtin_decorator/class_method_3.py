class Employee:
    company="cisco"
    @classmethod
    def show_company(cls):
        print(cls.company)

e1=Employee()
print(e1.company) #instance variable
print(Employee.company) #class variable

#Instance variables do NOT change class variables
e1.company="Comcast"
print(Employee.company) #class variable
print(e1.company)

