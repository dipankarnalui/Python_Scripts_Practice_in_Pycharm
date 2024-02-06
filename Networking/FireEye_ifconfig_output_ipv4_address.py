import subprocess

cmd = ['ipconfig']
#store the output of ipconfig into output.txt
with open('output.txt', 'w') as out:
    result = subprocess.call(cmd, stdout=out)

ip_list=[]
interface_list=[]
lines= open("output.txt").read().splitlines()
for line_no,line in enumerate(lines):
    if not line.startswith(" ") and line.endswith(":"): #interface name endswith :
        second_line = lines[line_no + 2].strip()#to get the next two lines of interface
        if "disconnected" in second_line:#to check if the interface is disconnected
            continue
        else:
            # if the interface is not disconnected then store into list
            interface_list.append(line)
    if "IPv4" in line:
        ip=line.split(":")[1]
        ip_list.append(ip)

for no, interface in enumerate(interface_list):
        print(interface, ip_list[no])


