#string reverse with -1
s1="Hello World"
print(s1[::-1])


#string reverse without -1
s2="Dipankar Nalui"

length=len(s2)
print(length)
#start,stop,step
for i in range(-1,-(length+1),-1):
    print(s2[i], end="")

#another approach
s3="interview"
len1=len(s3)
print(len1)
#start=last element
#stop=first element
#step=1 step backward
for i in range(len(s3)-1,-1,-1):
    print(s3[i],end="")

