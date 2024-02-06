grp1 = {"blr","chn","mum","del"}
grp2 = ["pune","tpuram","blr","hyd"]
#common = {"blr"}
common = grp1 & set(grp2)
print(common)