class Express:
  def set_avalue(self,a):
      self.a = a
      self.res = 0
  def set_bvalue(self,b):
      self.b = b
  def find_expression(self):
      self.res = self.a + self.b
  def showresult(self):
      print(self.res)


ob1 = Express()       # instaniate the class

'''
# we write
object.METHODNAME(ARGS)    # C++/JAVA/C++ - Object Oriented

# compiler interprets
classname.METHODNAME(object, ARGS)

ob1.set_avalue(10)    # Express.set_avalue(ob1,10) 
ob1.set_bvalue(20)    # Express.set_bvalue(ob1,20)
ob1.showresult()      # Express.showresult(ob1)
ob1.find_expression() # Express.find_expression(ob1)

ob1.showresult()    


'''


