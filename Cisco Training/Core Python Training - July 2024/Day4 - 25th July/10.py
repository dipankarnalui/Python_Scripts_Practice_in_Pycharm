class Account:
    def setrecord(self,name,type,bal):
        self.name = name # initialize data member-1
        self.type = type # initialize data member-2
        self.bal = bal # initialize data member-3
    def show(self):
        print("NAME =",self.name)
        print("TYPE =",self.type)
        print("BAL =",self.bal)


# create a instance or object
acc1 = Account()

# invoke the methods
acc1.setrecord("ravi","sb",25000)
acc1.show()
