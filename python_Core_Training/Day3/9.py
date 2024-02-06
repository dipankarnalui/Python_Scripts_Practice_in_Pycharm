class Product:
   def __init__(self,name):
       self.name = name               # INSTANCE DATA MEMBER
   def show(self):
       print("NAME = ",self.name)     # INSTANCE METHOD
   # def __eq__(self,other):
   #     return "HELLO WORLD"
p1 = Product("A")
p2 = Product("B")
p1.show()
p2.show()
print(p1==p2)