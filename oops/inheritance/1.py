class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        self.c=self.a+self.b
        print(self.c)

class child(calculator):
    pass

c_obj=child(1,2)
c_obj.add()