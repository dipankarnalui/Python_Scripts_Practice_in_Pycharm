data1="ravi-math=60,sci=20,soc=30"
data2="hari-math=15,sci=30,soc=45"

ravi_math,ravi_sci,ravi_soc=data1.split(",")
ravi_total=int(ravi_math.split("=")[-1]) + int(ravi_sci.split("=")[-1]) + int(ravi_soc.split("=")[-1])
print(ravi_total)

hari_math,hari_sci,hari_soc=data2.split(",")
hari_total=int(hari_math.split("=")[-1]) + int(hari_sci.split("=")[-1]) + int(hari_soc.split("=")[-1])
print(hari_total)

if ravi_total < hari_total:
   print("hari has scored better than ravi")
else:
   print("ravi has scored better than hari")

