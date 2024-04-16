d1={"a":"1",
    "b":"2",
    "c":"3"}
print(d1)

l1=[]
for k in d1.keys():
    print(k)
    l1.append(k)
print(l1)

print(l1[::-1])