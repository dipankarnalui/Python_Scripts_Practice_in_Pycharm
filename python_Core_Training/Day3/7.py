class Product:
   mesg = "this is a product class"    # Class Data member
   def __init__(self,name):
       self.name = name               # INSTANCE DATA MEMBER
   def show(self):
       print("NAME = ",self.name)     # INSTANCE METHOD
p1 = Product("A")
p2 = Product("B")
p1.show()
p2.show()
print(Product.mesg)