num =10
print(id(num))
tmp=num
print(id(tmp))
print(num is tmp)

sam = 10
print(id(sam))
print(num is sam)

big = 235676
print(id(big))
print(big is sam)

name1="dipankar"
print(id(name1))
print(num is name1)

name2="dip"
print(id(name2))
print(name1 is name2)

name3="sip"
print(id(name3))
print(name2 is name3)
