class A():
    def __init__(self,a,b): #a and b are parameters
        self.a=a # self.a = instance variable
        self.b=b # self.b = instance variable
    def add(self):
        return self.a+self.b
obj=A(10,20)
result=obj.add()
print(result)
