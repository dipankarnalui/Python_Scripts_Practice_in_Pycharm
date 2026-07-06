# give the NeighborID where state is not full.

ospf_output = """

Neighbor ID     Pri   State           Dead Time   Address         Interface

10.1.1.1        1     FULL/DR         00:00:34    192.168.1.1     GigabitEthernet0/0

10.1.1.2        1     INIT/DROTHER    00:00:35    192.168.1.2     GigabitEthernet0/1

10.1.1.3        1     FULL/BDR        00:00:33    192.168.1.3     GigabitEthernet0/2

10.1.1.4        1     2WAY/DROTHER    00:00:31    192.168.1.4     GigabitEthernet0/3

"""

import re
s1= ospf_output.strip()
#print(s1)
#print(type(s1))
for line in s1.splitlines():
    #print(line)
    if re.search("FULL",line):
        #print(line)
        words_list=line.split()
        #print(words_list)
        print(words_list[0])



