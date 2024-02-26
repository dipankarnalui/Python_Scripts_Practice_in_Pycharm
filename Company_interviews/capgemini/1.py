class Cal():
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        return c
    def sub(self):
        c=self.a - self.b
        return c
class CalB(Cal):
    pass
a=10
b=23
obj=Cal(a,b)
#result1=obj.add()
#result2=obj.sub()
#print(result1)
#print(result2)

#Child class inherits the properties of parent class Cal()
obj2=CalB(a,b)
result1=obj2.add()
result2=obj2.sub()
print(result1)
print(result2)

