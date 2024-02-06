class Person:
  def __init__(self,name,loc):
      self.name = name
      self.loc  = loc
  def show(self):
      print(self.name,self.loc)
  def __eq__(self,other):
      print("equal-to operator is called")
      if self.name==other.name and self.loc==other.loc:
         return True
      else:
         return False
p1 = Person("ravi","blr")
p2 = Person("ravi","blr")
if p1==p2:     # p1.__eq__(p2)
               # compare the address of p1 & address of p2
   print("Equal")
else:
   print("Unequal")