class Emp:
    sal = 0
    count = 0
    def __init__(self, name,sal):
        self.name=name
        self.sal=sal
        Emp.count = Emp.count + 1
        Emp.sal = Emp.sal + Emp.sal
    @classmethod
    def display_avg_salary(cls):
        avg=Emp.sal / Emp.count
        print(avg)
eob1 = Emp("ravi",15000)
eob2 = Emp("john",25000)

Emp.display_avg_salary()   # ? 20K

eob3 = Emp("hari",23000)
Emp.display_avg_salary()   # ? 21K

del eob1
del eob2
Emp.display_avg_salary()   # ? 23k

'''
Hint:  class data member   - & Class methods
       ctor & Dtor
'''