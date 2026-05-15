class Calculator():
    def __init__(self,name):
        self.company_name = name #instance variable

#Both objects have different company.
ob1=Calculator("cisco")
print(ob1.company_name)
ob2=Calculator("comcast")
print(ob2.company_name)



