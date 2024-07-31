class Account():
    def setrecord(self,name,type,balance):
        self.name=name
        self.type=type
        self.balance=balance
    def show(self):
        print(self.name)
        print(self.type)
        print(self.balance)
    def deposit(self,amt):
        self.balance=self.balance+amt
    def withdraw(self,amt):
        self.balance = self.balance - amt
    def checkbal(self):
        print(self.balance)
    def transfer(self,acc2,amt):
        acc2.balance=acc2.balance + amt
        self.balance=self.balance - amt

acc1 = Account()
acc1.setrecord(name="ravi",type="sb",balance=25000)
acc1.show() # name = ravi type = sb balance = 25000
acc1.deposit(5000)
acc1.checkbal() # balance = 30000
acc1.withdraw(2000)
acc1.checkbal() # balance = 28000

acc2 = Account()
acc2.setrecord("manu","sb",45000)
acc1.transfer(acc2,5000) # from acc1 to acc2 5k
acc1.checkbal() #balance = 23000
acc2.checkbal() #balance = 50000

