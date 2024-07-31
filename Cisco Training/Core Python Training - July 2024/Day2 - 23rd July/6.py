data1="ravi-math=60,sci=20,soc=30"
data2="hari-math=15,sci=30,soc=45"

marks1= data1.replace('=',',').split(',')[1::2]
marks2= data2.replace('=',',').split(',')[1::2]

if sum(list(map(int,marks1))) == sum(list(map(int,marks2))):
    print("Both scored Equal")
elif sum(list(map(int,marks1))) < sum(list(map(int,marks2))):
    print("Hari Scored Better tahn Ravi")
else:
    print("Ravi scored better than Hari")
