#shallow copy
a=[10,20,30,40,50]
b=a
print(a)
print(b)
a[0]=0
a[1]=0
a[2]=0
print(a)
print(b)