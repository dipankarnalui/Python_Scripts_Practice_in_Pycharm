class Account:
    def __init__(self):
        self.name=None 
        self.type=None 
        self.balance=0   
    def setrecord(self,name, type,balance):
        self.name=name
        self.type=type
        self.balance=balance             
    def show(self):
        print(f"name= {self.name}, type= {self.type}, balance={self.balance}")
    def deposit(self,amount):
        self.balance=self.balance+amount 
    def checkbal(self):
        print(f"balance = {self.balance}")
    def withdraw(self, amt):
        self.balance=self.balance - amt 
    def checkbal(self):
        print("balance = ",self.balance)
    def transfer(self,obj,amnt):
        obj.balance=self.balance-amnt  
acc1 = Account()
acc1.setrecord(name="ravi",type="sb",balance=25000)
acc1.show()            # name = ravi type = sb  balance = 25000
acc1.deposit(5000)     # money deposited 
acc1.checkbal()        # balance = 30000
acc1.withdraw(2000)    # money withdrawn
acc1.checkbal()        # balance = 28000

acc2 = Account()
acc2.setrecord("manu","sb",45000)
acc1.transfer(acc2,5000)  # from acc1 to acc2 5k 
acc1.checkbal()    #balance = 23000  
acc2.checkbal()    #balance = 50000

