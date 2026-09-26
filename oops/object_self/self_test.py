class A():
    def set_name(self,name):
        self.name=name
    def get_name(self):
        print(self.name)
obj=A()
A.set_name(obj,"Dipankar") #self = obj
A.get_name(obj)

