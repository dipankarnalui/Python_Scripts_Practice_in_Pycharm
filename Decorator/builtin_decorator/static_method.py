class A:
    def __init__(self):
        print("A")
    @staticmethod
    def add(a,b):
        return a+b

obj=A()
r=obj.add(1,2)
print(r)




