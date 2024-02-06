class Product:
   mesg = "this is a product class"    # Class Data member
   def __init__(self,name):
       self.name = name               # INSTANCE DATA MEMBER
   def show(self):
       print("NAME = ",self.name)     # INSTANCE METHOD
   @classmethod
   def display(cls):
       print(cls)
       print(cls.mesg)
Product.display()
p1 = Product("A")
p2 = Product("B")
p1.show()
p2.show()