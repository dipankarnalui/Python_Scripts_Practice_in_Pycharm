class Account:
    def setrecord(self,name,type,balance):
        self.name=name
        self.type=type
        self.balance=balance

    def show(self):
        print("Name: ",self.name)
        print("Type: ",self.type)
        print("Balance",self.balance)

    def deposit(self,amt):
        self.balance = self.balance+amt

    def withdraw(self,amt):
        self.balance = self.balance-amt

    def transfer(self,a2,amt):
        self.withdraw(amt)
        a2.deposit(amt)
    def chk_bal(self):
        print("Balance",self.balance)

