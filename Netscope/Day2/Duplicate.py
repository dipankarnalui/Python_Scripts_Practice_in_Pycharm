# given an array find all the duplicates and print as a dictionary
IP=[2,8,1,1,5,8,8]
# OP : {8:3, 1:2}
cnt=0
d={}
for i in range(0,len(IP)):
    if IP.count(IP[i]) > 1:
        print(IP[i])
        k=IP[i]
        v=IP.count(IP[i])
        d[k]=v
print(d)

