import re
class Product:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

    def getname(self):
        return self._name

    def setname(self, name):
        if not re.search("[0-9]", str(name)):
            self._name = name
        else:
            self._name = "BLANK"

    name = property(getname, setname)


p1 = Product("HDD")  # ?
p1.show()
print(vars(p1))
p1.name = 1234
print(vars(p1))

p2 = Product(1234)  # ?
p2.show()
p3 = Product("HDD123")  # ?
p3.show()
p4 = Product(2.5)  # ?
p4.name = 12345
p4.show()