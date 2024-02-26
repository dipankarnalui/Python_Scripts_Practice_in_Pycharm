#Juniper interview with Varun 
#write a code to find the positions of the elements whose sum value is the target value 
list1=[2,4,5,6]
target = 10

#output=[1,3]


for i in range(0,len(list1)):
    j=i+1
    for k in range(j,len(list1)):
        if list1[i] + list1[k] == target:
            #print(list1[i],list1[k])
            print(i,k)