class Test:
    def __init__(self,a):
        print("constructor called")
        self.a=a
    def sqare(self):
        c=a**2 #c is instance variable
        return c
a=20
ob=Test(a)
res=ob.sqare()
print(res)

