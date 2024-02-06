class Person:
    def __init__(self, name, age, address, mobile):
        self.name1=name
        self.age1=age
        self.address1=address
        self.mobile1=mobile

    def display(self):
        print(self.name1, self.age1, self.address1, self.mobile1)

    def show(self):
        print(self.name1)

class Employee(Person):
    pass

p1=Person("Dipankar",30,"Bangalore",7639970299)
p1.display()
p1.show()

#child class object also can access the parent class variables and methods
e1=Employee("Dipankar",30,"Bangalore",7639970299)
e1.display()
e1.show()