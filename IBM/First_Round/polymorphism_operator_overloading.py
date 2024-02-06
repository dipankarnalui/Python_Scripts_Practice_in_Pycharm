#polymorhiism
#operator overloading
class PolyTest:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c= self.a + self.b
        return c

a="hello "
b="world"
obj=PolyTest(a,b)
r=obj.add()
print(r)

a=2
b=3
obj=PolyTest(a,b)
r=obj.add()
print(r)
