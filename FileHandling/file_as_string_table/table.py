import re

ospf_output = """
NeighborID Pri State DeadTime Address Interface
10.1.1.1 1 FULL/DR 00:00:34 192.168.1.1 GigabitEthernet0/0
10.1.1.2 1 INIT/DROTHER 00:00:35 192.168.1.2 GigabitEthernet0/1
10.1.1.3 1 FULL/BDR 00:00:33 192.168.1.3 GigabitEthernet0/2
10.1.1.4 1 2WAY/DROTHER 00:00:31 192.168.1.4 GigabitEthernet0/3
"""

columns = {
    "NeighborID": [],
    "Pri": [],
    "State": [],
    "DeadTime": [],
    "Address": [],
    "Interface": []
}

data_list=ospf_output.strip().splitlines()[1:]
#print(data_list)

for rows in data_list:
    #print(rows)
    cols=rows.split()
    #print(cols)
    columns["NeighborID"].append(cols[0])
    columns["Pri"].append(cols[1])
    columns["State"].append(cols[2])
    columns["DeadTime"].append(cols[3])
    columns["Address"].append(cols[4])
    columns["Interface"].append(cols[5])

print(columns)

print(columns["NeighborID"])
