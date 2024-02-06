#print largest element from the list
#if the largest element is present multiple positions, print the positions
#Also print how many times the it is present
l1=[10,7,3,20,5,30,5,7,30,2,5,6,30]
largest= l1[0] #let's assume the first element if the largest
for i in range(0, len(l1)):
    #compare with next element
    if largest < l1[i]:
        largest = l1[i]
print("Largest element is ", largest)
print("It is present {} times".format(l1.count(largest)))
print("Found first occrrence at = {}".format(l1.index(largest)))
count = 0
for i in range(0,len(l1)):
    if l1[i] is largest:
        print("largest element {} is found at {} position".format(largest,i))
        count=count+1
print("Total occrrences = {}".format(count))

