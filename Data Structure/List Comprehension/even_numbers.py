l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

odd= [ l1[i] for i in range(len(l1)) if l1[i]%2!=0 ]
print(odd)

even = [ l1[i] for i in range(len(l1)) if l1[i]%2==0 ]
print(even)

