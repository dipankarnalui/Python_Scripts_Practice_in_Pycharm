num1=10
num2=20
res=num1 + num2

print(res)  
print("Result is ",res)         # prefered way
print("Result is "+str(res))
print("Result is "+repr(res))

#Place Holders
#---------------
print("sum of %s and %s is %s" %(num1,num2,res))
print("sum of {0} and {1} is {2}".format(num1,num2,res))
print(f"sum of {num1} and {num2} is {res}")
