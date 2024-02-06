class calculator():
    def __init__(self,a1,b1):
        self.a=a1
        self.b=b1

    def add(self):
        c=self.a + self.b
        return c

    def multiply(self):
        c=self.a * self.b
        return c

    def subtract(self):
        if self.a > self.b :
            c = self.a - self.b
        elif self.a < self.b :
            c = self.b - self.a
        else:
            c = 0
        return c

a=20
b=30
calobj=calculator(a,b)
add_res=calobj.add()
mul_res=calobj.multiply()
sub_res=calobj.subtract()

print("Add result = ", add_res)
print("Mul result = ", mul_res)
print("Sub result = ", sub_res)
