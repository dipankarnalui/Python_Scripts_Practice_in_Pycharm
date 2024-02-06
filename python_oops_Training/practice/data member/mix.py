class Test:
    d=1 #class variable
    def __init__(self,a):
        print("constructor called")
        self.a=a
    def sqare(self):
        c=a**2 #c is instance variable
        print("c = ",c)
        self.c=c
        return c
    def cube(self):
        f=a**3 #f is instance variable
        return f
    def class_variable_print(self):
        print("class variable d = ",Test.d)
    def access_both_data_member(self):
        print(" d +  c = ", Test.d + self.c)
a=4
ob=Test(a)
res=ob.sqare()
print(res)
cube_res=ob.cube()
print(cube_res)
ob.class_variable_print()
ob.access_both_data_member()
