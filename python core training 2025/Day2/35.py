# <function_name> = lambda <arguments parameter> :  <return statement>

f1 = lambda argument : argument.split(' ')[1]
print(f1("ravi kumar"))

f2 = lambda argument : argument.split(' ')[0][0].upper() + argument.split(' ')[1][0].upper() 
print(f2("ravi kumar"))

f3 = lambda argument : argument.split(' ')[0][0].upper() + argument.split(' ')[0][1:] + " " +  argument.split(' ')[1][0].upper() + argument.split(' ')[1][1:]
print(f3("ravi kumar"))

f4 = lambda argument : sorted(argument)
print(f4([40,50,10,20]))

f5 = lambda argument : list(map(int,argument.replace("-",",").split(",")[2:]))
print(f5("ravi-blr-10,20,30"))

f6 = lambda argument : list(map(str,argument.replace("-",",").split(",")[2:]))
print(f6("ravi-blr-10,20,30"))

f7 = lambda argument : list(map(int,argument.replace("-",",").split(",")[2:]))
print(f7("ravi-blr-10,20,30"))

f8 = lambda argument : sum(list(map(int,argument.replace("-",",").split(",")[2:])))
print(f8("ravi-blr-10,20,30"))

