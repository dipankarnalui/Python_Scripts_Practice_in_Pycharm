str1="hello World"
l1=str1.split()
print(l1)

l2=[]
for i in range(len(str1)):
    if str1[i] != ' ':
        l2.append(str1[i])
print(l2)
