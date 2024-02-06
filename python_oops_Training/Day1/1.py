class Person:
   def setdetails(self,name,dob,loc):
       self.name = name   # data members are initialized
       self.dob  = dob    # data members are initialized
       self.loc  = loc    # data members are initialized
   def show(self):
       print("Name = ",self.name)  # display data mem-1
       print("DOB  = ",self.dob)   # display data mem-2
       print("LOC  = ",self.loc)   # display data mem-3
   def convert(self):
       self.name = self.name.upper()  # operation on datamem

# main program
ravi = Person()   # instance of class - OBJECT memory allocated
guru = Person()   # instance of class - OBJECT memory allocated

# set the data members via methods
ravi.setdetails("ravi","12/12/2000", "blr")
guru.setdetails("guru","10/11/2001", "chn")

# verify
ravi.show()
guru.show()

#address
print(id(ravi))
#Classname
print(ravi.__class__)
print(type(ravi))
#Data Member
print(vars(ravi))
print(ravi.__dict__)
#Data Memer & Mem func
print(dir(ravi))

#to remove built-in methods... dunder method...
print([elem for elem in dir(ravi) if not str(elem).startswith("_")])
fns = [elem for elem in dir(ravi) if not str(elem).startswith("_")]
data_mem =list(vars(ravi).keys())
print("METHOD NAME = ",set(fns)-set(data_mem))

