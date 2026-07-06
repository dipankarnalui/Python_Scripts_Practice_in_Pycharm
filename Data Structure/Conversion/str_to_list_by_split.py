ospf_output = """

Neighbor ID     Pri   State           Dead Time   Address         Interface

10.1.1.1        1     FULL/DR         00:00:34    192.168.1.1     GigabitEthernet0/0

10.1.1.2        1     INIT/DROTHER    00:00:35    192.168.1.2     GigabitEthernet0/1

10.1.1.3        1     FULL/BDR        00:00:33    192.168.1.3     GigabitEthernet0/2

10.1.1.4        1     2WAY/DROTHER    00:00:31    192.168.1.4     GigabitEthernet0/3

"""

s1= ospf_output.strip()

for line in s1.splitlines():
    if line.strip():
        if "Neighbor" not in line:
            neighbor,pri,state,dead,address,interface = line.split()
            if "FULL" in state:
                print(neighbor)

