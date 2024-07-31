d1={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
}
for e in d1:
    print(e,d1[e])
print("------------")
for k,v in d1.items():
    print(k,v)
print("------------")

l1=list(d1.items())
print(l1)