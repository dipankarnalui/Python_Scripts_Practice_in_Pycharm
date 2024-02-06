#write a code to display the ipv4 address from ipconfig command
import subprocess

cmd = ['ipconfig']

with open('output.txt', 'w') as out:
    result = subprocess.call(cmd, stdout=out)

ip_list=[]
interface_list=[]
with open('output.txt', 'r') as file1:
    lines = file1.readlines()
    for line in lines:
        if not line.startswith(" "):
            print(line)
            interface_list.append(line)
        if "IPv4" in line:
            print(line)
            ip=line.split(":")[1]
            ip_list.append(ip)
'''            
for ip in ip_list:
    print(ip)
for i in interface_list:
    print(i.strip())
'''

