class Product:

    def __init__(self, name, ctgry, qty):
        self.name = name
        self.ctgry = ctgry
        self.qty = qty

    def show(self):
        print("%s %s %s" %(self.name, self.ctgry, self.qty))


p1 = Product("HDD", "storage", 10)
p1.show()          # name=HDD ctgry=storage qty=10
print(vars(p1))    # {name : HDD, ctgry : storage, qty : 10}
p1.company = "WD"  # data member already exists
                   # over-write
                   # if not create new data member
print(vars(p1))    # {name:HDD,ctgry:storage,qty:10,company:WD}
p1.show()          # will it display thew new DATA MEMBER ?

# replace functionality of "show()" with new functionality

# normal function
def anothershow(self):
    print("%s %s %s" % (self.name, self.ctgry, self.qty))
    print(self.company)

oldaddress = Product.show
Product.show = anothershow
p1.show()   # will it display the "company" ?
Product.show = oldaddress
p1.show()


