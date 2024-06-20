nums=[3,4,9,1,3,9,5]
key=9
k=1

li=[]
for i in range(len(nums)):
    if nums[i] == key:
        li.append(i)
print(li)

for i in range(len(nums)):
    print("i=",i)
    for j in li:
        print("j=",j)
        print("|i-j|=", abs(i - j))
        if abs(i-j)<=k:
            print("{} is a k-distant index".format(i))