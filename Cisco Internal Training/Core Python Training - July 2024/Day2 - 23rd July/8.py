data1="ravi-math=60,sci=20,soc=30"
data2="hari-math=15,sci=30,soc=45"
data1=data1.replace("-",",").replace("=",",").split(",")[2::2]
data1=list(map(int, data1))
print(sum(data1))

data2=data2.replace("-",",").replace("=",",").split(",")[2::2]
data2=list(map(int, data2))
print(sum(data2))

if data1 > data2:
    print("ravi has scored better than hari")
else:
    print("hari has scored better than ravi")
