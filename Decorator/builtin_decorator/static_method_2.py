class Decorator_Test():
    def __init__(self):
        print("Decorator_Test")

    # static method does not contain self
    @staticmethod
    def sum(a,b): #without self
        return a+b

    #normal_method with self
    def normal_method(self,a,b):
        return a+b

d=Decorator_Test()
r=d.sum(1,2)
print(r)

r2=d.normal_method(3,5)
print(r2)



