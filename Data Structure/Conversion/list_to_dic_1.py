l1=['a','b','c','d']
l2=[1,2,3,4]
d1={}
if len(l1)==len(l2):
    for i in range(len(l1)-1):
        k,v=l1[i],l2[i]
        d1[k]=v
else:
    print("two lists are different size")
print(d1)