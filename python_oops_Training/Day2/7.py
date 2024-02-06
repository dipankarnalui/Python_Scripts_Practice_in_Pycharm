class Mtime:
    def __init__(self,hours,mins,secs):
        self.hours = hours
        self.mins = mins
        self.secs = secs
    def __add__(self,other):
        tmp=Mtime(0,0,0)
        tmp.hours=self.hours+other.hours
        tmp.mins=self.mins+other.mins
        tmp.secs=self.secs+other.secs
        return tmp
    def show(self):
        print(self.hours,":",self.mins,":",self.secs)

ob1 = Mtime(hours=10,mins=20,secs=30)
ob2 = Mtime(hours=1,mins=2,secs=3)
ob1.show()   # 10:20:30
ob2.show()   # 1:2:3
res = ob1 + ob2
res.show()   # 11:22:33
print(ob1)   # 10:20:30   # ob1.show()
print(ob2)   # 01:02:03   # ob2.show()
print(res)   # 11:22:33   # ob3.show()

'''
Hint     : def __add__(self,other)
         : we have override tostring in python
'''
