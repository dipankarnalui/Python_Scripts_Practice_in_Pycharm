#write a code to find the duplicate elemets and their positions and number of occurrences
a = [10,20,10,30]
b = []
for i in range(0,len(a)):
    if a.count(a[i]) > 1:
        print("The element " + str(a[i]) + " is found in the position "  + str(i))
        print("The element " + str(a[i]) + " is present " + str(a.count(a[i])) + " times")


for i in range(0,len(a)):
    if a.count(a[i]) > 1:
       b.append(a[i])
print(b)


