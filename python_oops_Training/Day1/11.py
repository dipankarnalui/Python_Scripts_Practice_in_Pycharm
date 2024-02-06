class TestCase:
    def __init__(self,name,expected,result):
        self.name=name
        self.expected= expected
        self.result = result
    def find_status(self):
        if self.expected == self.result:
            self.status="Pass"
        else:
            self.status="Fail"
        return self.name, self.status

    def show(self):
        if self.status == "Pass":
            print("Name = ", self.name, "Status = ", self.status)
        elif self.status == "Fail":
                print("Name = ", self.name, "Status = ", self.status)
t1 = TestCase(name="Memory", expected=100, result=50)
t2 = TestCase("Disk", 150, 150)
t3 = TestCase("CPU", 50, 50)
t4 = TestCase("ROM", 120, 100)
t5 = TestCase("I/o", 200, 200)
t6 = TestCase("Bus", 10, 0)
objlst = [t1,t2,t3,t4,t5,t6]
pass_lst = []
fail_lst = []
d1={}
for elem in objlst:
   name,status=elem.find_status()
   d1[name]=status
   print(d1)
   elem.show()

'''                          
if expected==result
    status = PASS
 else:
    status = FAIL

Memory - FAIL               
Disk   - PASS
CPU    - PASS
ROM    - FAIL
I/o    - PASS
Bus    - FAIL
print(pass_lst)    # ["Disk","CPU","I/o"]
print(fail_lst)    # ["Memory","ROM","Bus"]
'''

