f1 = lambda x :  print(x.split()[1])
f1("ravi kumar")

f2 = lambda x : print(x.split()[0][0].upper()+x.split()[1][0].upper())
f2("ravi kumar")

f3 = lambda x :  print(x.split()[0][0].upper()+x.split()[0][1:]+" "+x.split()[1][0].upper() + x.split()[1][1:])
f3("ravi kumar")

f4 = lambda x : print(sorted(x))
f4([40,50,10,20])

f5 = lambda x : print(x.split("-")[2])
f5("ravi-blr-10,20,30")

f6 = lambda x : print(x.split("-")[2].split(","))
f6("ravi-blr-10,20,30")

f7 = lambda x :  print(list(map(int,x.split("-")[2].split(","))))
f7("ravi-blr-10,20,30")

f8 = lambda x : print(sum(list(map(int, x.split("-")[2].split(",")))))
f8("ravi-blr-10,20,30")