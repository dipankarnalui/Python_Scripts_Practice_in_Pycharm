class PolyTest:
    def __init__(self):
        pass
    def add(self,a,b,c=1):
        r=a+b+c
        return r
obj=PolyTest()
r=obj.add(2,3,4)
print("three parameter = ",r)
s=obj.add(2,3)
print("two parameter = ",s)
