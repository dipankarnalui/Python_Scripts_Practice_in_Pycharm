'''
l1=[23,56,75,23,67,34,23,90,45,34,78,34,56,34,89,34,90,23,23]
#number_max_dup
#56 and 90 are present 2 times,
#23 is present 3 times
#34 is present 5 times
#Output will be 34
dup=[]
for i in range(0,len(l1)):
    j=i+1
    for k in range(j,len(l1)):
        if l1[i] == l1[k]:
            #print(l1[i])
            #if l1[i] not in dup:
            dup.append(l1[i])
print("All duplicate elements are {}".format(dup))
largest=0
for i in range(0,len(dup)):
    j=i+1
    for k in range(j,len(dup)):
        if dup.count(dup[i]) >= dup.count(dup[k]):
            largest= dup[i]
print(largest)
'''

###The above logic will have much time complexity because of using two for loops
## The below logic will reduce the time complexity as we do not use nested for loop

l1=[23,56,75,23,67,34,23,90,45,34,78,34,56,34,89,34]
duplicate=[]
for i in range(0,len(l1)):
    if l1.count(l1[i]) > 1:
        duplicate.append(l1[i])
print("Duplicate elements => ", duplicate)

dict1 = {}
for i in range(0,len(duplicate)):
    #print(str(duplicate[i]) + " is present " + str(l1.count(duplicate[i])) + " times")
    #print(duplicate[i] , l1.count(duplicate[i]) )
    dict1.update({ duplicate[i] : l1.count(duplicate[i]) })
    #dict1.update( { key : value } )

print("Duplicate Elements count ==> ", dict1)

#print(max(dict1.values()))

#how to get the max key and value from dictionary in one line
print("The duplicate element which is present max times => " , max(dict1, key=dict1.get))

'''
for key, value in dict1.items():
    print(key,value)
'''