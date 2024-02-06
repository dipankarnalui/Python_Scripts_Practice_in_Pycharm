class Product:
    total = 0  # class data member

    # anything defined here is a class datamember
    def __init__(self, name, ctgry, qty):
        self.name = name
        self.ctgry = ctgry
        self.qty = qty
        Product.total += self.qty  # totaling all the qty

    def show(self):
        print("%s %s %s" % (self.name, self.ctgry, self.qty))

    @classmethod  # Special syntax to define class methods
    def display(cls):
        print("CLS=", cls)
        print("Total =", cls.total)
        print("Total =", Product.total)

Product.display()
p1 = Product("CPU", "c1", 10)
p2 = Product("MON", "c2", 10)
p3 = Product("HDD", "c1", 10)
p4 = Product("PRN", "c3", 10)
p1.display()  # Product.display()
