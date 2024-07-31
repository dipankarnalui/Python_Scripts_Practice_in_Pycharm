'''
compare total marks of ravi & hari
display message
hari has scored better than ravi
or
ravi has scored better than hari
'''

data1="ravi-math=60,sci=20,soc=30"
data2="hari-math=15,sci=30,soc=45"
words1=data1.split(",")
ravi= [int(e.split("=")[1]) for e in words1]
print(ravi)
words2=data2.split(",")
hari= [int(e.split("=")[1]) for e in words2]
print(hari)
if sum(ravi) > sum(hari):
    print("ravi has scored better than hari")
else:
    print("hari has scored better than ravi")