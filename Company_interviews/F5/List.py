l1 = ["sting", 123,"buvana","dipankar",12345]
l1.append("amma")
print(l1)
x=l1.copy()
print(x)
x.clear()
print(x)
print(l1)
print(l1.count(123))
l1.reverse()
print(l1)
l2 =["expending",123]
l1.extend(l2)
print(l1)
l1.pop(1)
print(l1)
l1.remove(123)
print(l1)
print(l1)


x=10
y=20
t=x
x=y
y=t
print(x)
print(y)

l2 =[4,5,1,3,2]
for i in range(0,len(l2)):
    for j in range(0,len(l2)):
        if l2[i] > l2[j]:
            t=l2[j]
            l2[j]=l2[i]
            l2[i]=t
print(l2)






