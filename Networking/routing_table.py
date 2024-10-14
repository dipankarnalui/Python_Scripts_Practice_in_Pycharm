'''
dipankar@CSCO-W-PF4HTZD2:/mnt/c/Users/dnalui$ ip route
default via 172.23.0.1 dev eth0 proto kernel
172.23.0.0/20 dev eth0 proto kernel scope link src 172.23.6.250
dipankar@CSCO-W-PF4HTZD2:/mnt/c/Users/dnalui$
dipankar@CSCO-W-PF4HTZD2:/mnt/c/Users/dnalui$ netstat -r
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         172.23.0.1      0.0.0.0         UG        0 0          0 eth0
172.23.0.0      0.0.0.0         255.255.240.0   U         0 0          0 eth0
dipankar@CSCO-W-PF4HTZD2:/mnt/c/Users/dnalui$
'''

#print the Gateways only using python
