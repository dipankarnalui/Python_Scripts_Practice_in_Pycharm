class Mycalculator:
    def __init__(self,a,b):
        print("contructor called")
        self.a=a
        self.b=b
    def add(self):
        print("add method")
        self.c=self.a + self.b
        return self.c
a=10
b=50
ob=Mycalculator(a,b)
c=ob.add()
print("result = ", c)
