str="""
NAME=Red Hat Enterprise Linux
VERSION=8.2
NUAGE_RPM=765
6WIND_VERSION=3.4.3
MGMT_IP_ADDRESS=192.168.32.1
NO_OF_VMS=10
"""
d1={}
all_lines = str.strip().splitlines()
for line in all_lines:
    key=line.split("=")[0]
    val = line.split("=")[1]
    #print(key,val)
    #d1.update({key:val})
    d1[key]=val
print(d1)


