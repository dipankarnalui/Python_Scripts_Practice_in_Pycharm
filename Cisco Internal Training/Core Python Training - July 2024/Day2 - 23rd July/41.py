'''
f1("ravi kumar") - kumar
f2("ravi kumar") - RK
f3("ravi kumar") - Ravi Kumar
f4([40,50,10,20]) - [10,20,40,50]
f5("ravi-blr-10,20,30") - "10,20,30"
f6("ravi-blr-10,20,30") - ["10","20","30"]
f7("ravi-blr-10,20,30") - [10,20,30]
f8("ravi-blr-10,20,30") - 60
'''
def f1(x):
    print(x.split()[1])
f1("ravi kumar")
def f2(x):
    print(x.split()[0][0].upper()+x.split()[1][0].upper())
f2("ravi kumar")
def f3(x):
    print(x.split()[0][0].upper()+x.split()[0][1:]+" "+x.split()[1][0].upper() + x.split()[1][1:])
f3("ravi kumar")
def f4(x):
    x.sort()
    print(x)
f4([40,50,10,20])
def f5(x):
    print(x.split("-")[2])
f5("ravi-blr-10,20,30")
def f6(x):
    print(x.split("-")[2].split(","))
f6("ravi-blr-10,20,30")
def f7(x):
    print(list(map(int,x.split("-")[2].split(","))))
f7("ravi-blr-10,20,30")
def f8(x):
    print(sum(list(map(int, x.split("-")[2].split(",")))))
f8("ravi-blr-10,20,30")