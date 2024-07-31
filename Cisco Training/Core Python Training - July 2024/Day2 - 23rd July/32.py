l1=["blr","50","chn","10","30","20","abc","xyz"]
r=[]
for e in l1:
    if e.isdigit():
        r.append(int(e))
print(r)
r.sort()
print(r)
print(sum(r))

