#string operations without using list
x = "AAABBCCAADDV"
out = "A5B2C2D2V1"
s1=''
for e in x:
    store=e + str(x.count(e))
    if store not in s1:
        s1 = s1 + store
print(s1)