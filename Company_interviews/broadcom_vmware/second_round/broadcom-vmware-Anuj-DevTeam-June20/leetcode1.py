target=0
nums=[-1,0,1,2,-1,-4,0,0]
l1=[]
l2=[]
for i in range(len(nums)):
    j=i+1
    for j in range(i+1,len(nums)):
        k=j+1
        for k in range(j+1,len(nums)):
            if nums[i] + nums[j] + nums[k] == target:
                l1=[i,j,k]
                l2.append(l1)
                print("i= {} , j= {}, k={}".format(i,j,k))
                print("nums[i]= {} , nums[j]= {}, nums[k]= {}".format(nums[i],nums[j],nums[k]))
                print("nums[i] + nums[j] + nums[j] = {}".format(nums[i] + nums[j] + nums[k]))
print(l2)
