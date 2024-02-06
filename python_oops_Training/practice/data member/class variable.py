class CheckDataMember:
    a=10 #class variable
    b=20 #class variable
    def __init__(self):
        print("contructor called")
    def MemberFunction(self):
        print("Member function called")
    def printValues(self): #member function
        print("a = ", CheckDataMember.a) #using classname
        print("b = ", CheckDataMember.b)
        print("using self, a = ", self.a) #using self
        
ob=CheckDataMember()
ob.printValues()
