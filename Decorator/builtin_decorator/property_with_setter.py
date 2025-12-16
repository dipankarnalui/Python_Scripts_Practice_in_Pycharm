class Person:
    def __init__(self,a):
        self.a=a

    @property
    def age(self):
        return self.a

    @age.setter
    def age(self,value):
        self.a=value

p=Person(5)
print(p.age)
