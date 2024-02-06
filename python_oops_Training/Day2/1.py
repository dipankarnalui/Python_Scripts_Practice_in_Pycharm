class Person:
    def __init__(self,name,loc):
        self.name= name
        self.loc=loc
    def show(self):
        print(self.name)
        print(self.loc)
class SwEngg(Person):
    def __init__(self, name, loc, company, domain):
        Person.__init__(self,name,loc)
        self.company = company
        self.domain = domain
    def display(self):
        print(self.company)
        print(self.domain)
class Student(Person):
    def __init__(self, name, loc, instname, grade):
        Person.__init__(self,name,loc)
        self.instname = instname
        self.grade = grade
    def printvalues(self):
        print(self.instname)
        print(self.grade)
ob1 = SwEngg("dipankar","BLR","cisco","networking")
ob2 = Student("dipankar","CHN","Vidyamandir","8")
ob1.show()      #name    = ? & loc   = ?
ob1.display()   #company = ? & domain= ?
ob2.show()         #name    = ? & loc  = ?
ob2.printvalues()  #instname= ? & grade= ?