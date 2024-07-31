data1="ravi-math=60,sci=20,soc=30"
data2="hari-math=15,sci=30,soc=45"

def totalmarks(data):
    return sum(list(map(lambda entry: int(entry.split("=")[1]), data.split("-")[1].split(","))))

ravi_marks = totalmarks(data1)
hari_marks = totalmarks(data2)

if(ravi_marks>hari_marks):
    print("Ravi has scored higher than Hari")
elif(ravi_marks<hari_marks):
    print("Hari has scored higher than Ravi")
else:
    print("Both Ravi and Hari have scored the same")


