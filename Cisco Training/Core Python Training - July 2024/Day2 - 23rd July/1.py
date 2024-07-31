#list vector to scaler string

#list of integers
l1=[10,20,30,40]
print(l1)

#convert into list of strings
l2=list(map(str,l1))
print(l2)

#join the iterable to form string
s1="-".join(l2)
print(s1)