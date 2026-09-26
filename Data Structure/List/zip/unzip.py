l1=[('A', 23, 'Mumbai'), ('B', 24, 'Delhi'), ('C', 25, 'Bangalore')]
#name,age,city=zip(*l1)
name,age,city=list(zip(*l1))
#name,age,city=list(zip(l1))
print(name)
print(age)
print(city)
