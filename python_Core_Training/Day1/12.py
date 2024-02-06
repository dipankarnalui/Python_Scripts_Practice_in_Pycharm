grp1 = ["blr-10","chn-20","mum-30","del-40"]
grp2 = ["pune-10","tpuram-30","BLR-40","hyd-50"]

def f(grp):
    l1=[]
    for ele in grp:
        a,b=ele.split("-")
        l1.append(a.lower())
    return set(l1)
common = f(grp1) & f(grp2)
print(common)

'''
grp1 = ["blr-10","chn-20","mum-30","del-40"]
grp2 = ["pune-10","tpuram-30","BLR-40","hyd-50"]
newgrp1 = { e.split("-")[0].lower() for e in grp1 }
newgrp2 = { e.split("-")[0].lower() for e in grp2 }
res = newgrp1 & newgrp2
print(res)
'''