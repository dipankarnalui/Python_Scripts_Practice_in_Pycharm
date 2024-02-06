###
## need to correct

class Decimal:
    def __init__(self, num):
        self.num = num
    def show(self):
        print("Decimal = ", self.num)
class Octal(Decimal):
    def __init__(self, num):
        self.oct = oct(self.num)
    def show(self):
        print(" Octal = ", self.oct)
class Hexa(Decimal):
    def __init__(self, num):
        self.hex = hex(self.num)
    def show(self):
        print(" Hexa = ", self.hex)
class Binary(Decimal):
    def __init__(self, num):
        self.num = bin(num)
    def show(self):
        print("basesystem = Binary")
        print(" Binary = ", self.num)

ob1 = Octal(25)
ob1.show()  # decimal = 25
            # Octal   = ?
ob2 = Hexa(10)
ob2.show()  # decimal = 10
            # Hexa    = A
ob3 = Binary(10)
ob3.show()  # decimal = 10
            # Binary  = 1010
#Hint:  readymade function - oct()/hex()/bin()

