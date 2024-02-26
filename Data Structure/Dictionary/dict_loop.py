d1={
"k1":"v1",
"k2":"v2",
"k3":"v3"}

#print only keys
for k in d1:
    print(k)
#below is also same
for key in d1.keys():
    print(key)
#print key+value
for item in d1.items():
    print(item)
#print only values
for v in d1.values():
    print(v)