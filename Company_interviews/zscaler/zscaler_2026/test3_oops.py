class Person():
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def show_details(self):
        print(self.age,self.name)

class Student(Person):
    def __init__(self,id,mark,age,name):
        super().__init__(age,name)
        self.id=id
        self.mark=mark
    def show(self):
        print(f"id={self.id},mark={self.mark}")
        print(self.age, self.name)

s=Student(10,2345,30,"Dipankar")
s.show()
