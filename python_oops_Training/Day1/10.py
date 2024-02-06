class Person:
   # paramterized ctor with default arguments
   def __init__(self,name="blank",loc="blr",age=0):
      self.name = name
      self.loc  = loc
      self.age  = age
   def show(self):
      print(self.name,self.loc,self.age)


p1 = Person()
p2 = Person("ravi")
p3 = Person("ravi","mum")
p4 = Person("ravi","mum",21)

p5 = Person(loc="delhi")
p6 = Person(age=18,name="hari",loc="noida")
p7 = Person(name="john")

for p in [p1,p2,p3,p4,p5,p6,p7]:
   p.show()

# blank blr 0
# ravi blr 0
# ravi mum 0
# ravi mum 21
# blank delhi 0
# hari noida 18
# john blr 0
