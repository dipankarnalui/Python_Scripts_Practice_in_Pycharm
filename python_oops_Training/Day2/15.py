import re
class Product:

    def __init__(self, name):
        if type(name)==str and re.search("^[a-z]+$", name,re.I):
           self.name = name
        else:
           self.name = "BLANK"

    def show(self):
        print("%s"  %(self.name))


p1 = Product("HDD")    # fine
p1.show()
p2 = Product(1234)     # fail
p2.show()
p3 = Product("HDD123") # fail
p3.show()
p4 = Product(2.5)      # Fail
p4.show()

p4.name = "123456"   # bypass the rules
p4.show()
