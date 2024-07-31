data1 = "ravi,JOHN,umesh,Deepak,Anit"
data2 = "aditya,Avinash,ravi,DEEPAK"
# step1 Conversion the string to lower case
data1 = data1.lower()
data2 = data2.lower()
# step2 delimited string should be split to a LIST
lst1 = data1.split(",")
lst2 = data2.split(",")
# step3 Conversion a list into a set
grp1 = set(lst1)
grp2 = set(lst2)
# step4 find the INTERSECTION two sets
common = grp1 & grp2
print(common)