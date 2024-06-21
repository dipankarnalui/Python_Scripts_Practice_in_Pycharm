num=input("Enter the numbers separated by comma = ")
l1=[]
for e in num.split(","):
    l1.append(int(e))
print(l1)
largest=l1[0]
for i in range(len(l1)):
    if l1[i] > largest:
        largest = l1[i]
print(largest)