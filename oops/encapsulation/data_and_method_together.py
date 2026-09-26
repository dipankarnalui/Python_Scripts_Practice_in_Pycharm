#Encasulation = Data + Method
#Hiding Data inside method using private variable
#no direct access to data
#Encapsulation = Data hiding + controlled access
#Encapsulation means wrapping data (variables) and the methods that operate on that data into a single unit (class), while controlling access to the data.


class BankAccount(): #this class wraps the data + method
    def __init__(self,balance):
        self.__balance=balance #hidden data #private variable

    def deposit(self,amount): #controlled way to modify it
        self.__balance = self.__balance + amount

    def check_balance(self): #how to access the hidden data
        print(self.__balance)

b=BankAccount(200)
b.deposit(100)
b.check_balance()


