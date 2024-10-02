import os

f=os.open("emp.txt",'r')
data=f.read()
print(data)
f.close()

