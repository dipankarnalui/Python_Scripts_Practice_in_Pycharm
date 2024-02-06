'''
l1=[0,1,2,3,4,5,6,7,8,9,10]
print(l1[::-1])


s="How Are You"
new=""
for e in s:
    if e.isupper():
        new = new + e.lower()
    else:
        new = new + e.upper()
print(new)


s="How Are You"
s2=s.swapcase()
print(s2)


s="This is a test. This is another test."
store=""
for e in s:
    if e.isalpha():
        if e not in store:
            store = store + e + str(s.count(e))
print(store)


s="This is a test. This is another test."
store={}
for e in s:
    if e.isalpha():
        if e not in store:
            store.keys()
print(store)
'''
#collections
#re
#file handling 