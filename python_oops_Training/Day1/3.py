class Express:
    def set_avalue(self,a):
        self.a=a
    def set_bvalue(self,b):
        self.b=b
    def find_expression(self):
        self.res= (self.a**2) + (2 * self.a * self.b ) + (self.b**2)
    def showresult(self):
        print("Result = ",self.res)
ob1 = Express()       # instaniate the class
ob1.set_avalue(10)    # initialize the value1
ob1.set_bvalue(20)    # initialize the value2
ob1.find_expression()   #a2+b2+2ab
ob1.showresult()