data1="ravi-math=60,sci=20,soc=30"
data2="hari-math=15,sci=300,soc=45"

data1 = data1.replace("-",",").replace("=",",")
data2 = data2.replace("-",",").replace("=",",")

total_ravi = sum([int(e) for e in data1.split(",")[2::2]])
total_hari = sum([int(e) for e in data2.split(",")[2::2]])

if total_ravi > total_hari:
   left = "ravi"
   right = "hari"
else:
   left = "hari"
   right = "ravi"

print(f"{left} has scored better than {right}")
   
