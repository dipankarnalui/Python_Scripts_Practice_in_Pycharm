class Account:
   def setrecord(self,name,type,bal):
       self.name = name
       self.type = type
       self.bal = bal        
   def deposit(self,amt):
       self.bal+=amt
   def withdraw(self,amt):
       if amt < self.bal:
          self.bal-=amt
       else:
          print("In-sufficient balance")
   def transfer(self,other,amt):
       self.balance = self.balance-amt
       other.balance = other.balance+amt
   def show(self):
       print(self.name,self.type,self.bal)
   def checkbalance(self):
       print(self.bal)
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