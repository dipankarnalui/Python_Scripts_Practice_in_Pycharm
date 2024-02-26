#swap
a=2
b=3
print("before swap")
print("a = ", a)
print("b = ", b)
#a,b=b,a
tmp=a
a=b
b=tmp
l1="after swap"
l2 = "a = " + str(a)
l3 = "b = " + str(b)
with open("store.txt", "w") as f:
    f.write(l1+"\n")
    f.write(l2+"\n")
    f.write(l3+"\n")
