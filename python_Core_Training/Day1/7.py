'''
f1("ravi kumar")  -  kumar
f2("ravi kumar")  -  RK
f3("ravi kumar")  -  Ravi Kumar
'''

f1 = lambda x : x.split(" ")[1]
#print(f1("ravi kumar"))
f2 = lambda x :  str(x.split(" ")[0][0].upper()) + str(x.split(" ")[1][0].upper())
#print(f2("ravi kumar"))
f3 = lambda x :  x.split(" ")[0][0].upper() + x.split(" ")[0][1:] + " " + x.split(" ")[1][0].upper() +  x.split(" ")[1][1:]
# alternative title x.title()
f3 = lambda x : x.title()
#print(f3("ravi kumar"))

'''
f4([40,50,10,20]) -  [10,20,40,50]
f5("ravi-blr-10,20,30")  - "10,20,30"
f6("ravi-blr-10,20,30")  - ["10","20","30"]
f7("ravi-blr-10,20,30")  - [10,20,30]
f8("ravi-blr-10,20,30")  -  60
'''
f4 = lambda x : sorted(x)
#print(f4([40,50,10,20]))

f5 = lambda x : x.split("-")[2]
#print(f5("ravi-blr-10,20,30"))

f6 = lambda x : list(map(str,x.split("-")[2].split(",")))
#print(f6("ravi-blr-10,20,30"))

f7 = lambda x : list(map(int,x.split("-")[2].split(",")))
#print(f7("ravi-blr-10,20,30"))

f8 = lambda x : sum(list(map(int,x.split("-")[2].split(","))))
print(f8("ravi-blr-10,20,30"))