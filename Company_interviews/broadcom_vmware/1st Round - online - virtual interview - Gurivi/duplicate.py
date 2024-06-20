str1="abcban"
l1=list(str1)
dup=[]
for e in l1:
    if l1.count(e)>1 and e not in dup:
        dup.append(e)
print(dup)

