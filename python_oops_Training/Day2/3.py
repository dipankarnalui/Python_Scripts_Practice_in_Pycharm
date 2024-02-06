class Alpha:
    def fun1(self):
        print("Alpha-Fun1")
    def fun2(self):
        print("Alpha-Fun2")
class Beta:
    def fun2(self):
        print("Beta-Fun2")
class Delta(Alpha, Beta):
    def fun3(self):
        print("Alpha-fun3")
    def fun2(self):
        super().fun2()  # cascade with base class
        Beta.fun2(self)  # cascade with base class
        print("Delta-Fun2")
class Omega(Delta):
    def fun4(self):
        print("Omega-fun4")
ob = Omega()
ob.fun2()
'''
Note:
super() is a
special
method in python
used
to
call
the
over - ridden
methods
within
the


class
    super().overriddenmethod()


super()
also
follows
MRO

Note:
while calling over-ridden methods
avoid
using


class name - prefered way is via - super() 
'''