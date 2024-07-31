grp1 = {"blr","chn","mum","del"}
grp2 = ["pune","tpuram","blr","hyd"]

#common = grp1&set(grp2)
#OR
#common = grp1.intersection(grp2)

grp1 = ["blr-10","chn-20","mum-30","del-40"]
grp2 = ["pune-10","tpuram-30","BLR-40","hyd-50"]

newgrp1 = { e.split("-")[0].lower() for e in grp1 }
newgrp2 = { e.split("-")[0].lower() for e in grp2 }

res = newgrp1 & newgrp2
print(res)

