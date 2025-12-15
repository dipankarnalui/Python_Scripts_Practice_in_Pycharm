class Person:
    def __init__(self,name,gender,age):
        self.ename=name
        self.egender=gender 
        self.eage=age
    def show(self):
        print(f"name={self.ename}, gender={self.egender}, age={self.eage}")
class Employee(Person):
    def __init__(self, name, gender, age,salary):
        Person.__init__(self, name, gender, age)
        self.esalary=salary
    def show(self): #method overriding 
        print("Hello")

e1 = Employee("Sam","M", 29,60000)
#print(f"name={e1.ename}, gender={e1.egender}, age={e1.eage}, salary={e1.esalary}")
e1.show()
