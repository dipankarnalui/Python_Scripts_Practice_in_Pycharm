l1=[1,2,3,4,5,8,34,53,24,10,32,8,1,1,7,36]
#l2=[]
'''
for i in range(0,len(l1)):
    if l1[i] > 20:
        l2.append(l1[i])
'''
#euivalent to the above code
l2 = [  l1[i] for i in range(0,len(l1)) if l1[i] > 20 ]
print("l2 = ",l2)

print(l1.count(1))
print(l1.index(32))
l3 = l2.copy()
print("l3 = " ,l3)
l3[0]=890 #This will replace the 0th position with new value
print("l3 = " ,l3)
l3.insert(2,79)
print("l3 = " ,l3)
l3.pop(1) #pop by index
print("l3 = " ,l3)
l3.remove(32) #remove by element
print("l3 = " ,l3)