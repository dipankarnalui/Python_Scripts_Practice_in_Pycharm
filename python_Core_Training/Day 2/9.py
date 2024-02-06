'''
Task:-
======
if u r on windows use "dir"
if u r on mac     use "ls -l"
run this command within python
&
capture the output of the command
rwxr--r-- 1 root  root  432    one.txt
r--r--r-- 1 root  root  1,500  two.txt
prepare a dictionary for files & exclude the directories
final = {
         "one.txt" : 432,
         "two.txt" : 1500
        }
print("Total bytes = ",sum(final.values()))
Duration : 10 mins
Time     : 12.30 to 12.40
hint     : import subprocess
           res  = subprocess.check_output("dir", shell=True).decode()
'''

import subprocess

res=subprocess.check_output("dir", shell=True).decode()
#print(res)
lines = res.split("\n")
len1=len(lines)
#print("Total lines ",len1)
line_num = 0
d={}
for line in lines:
    line_num = line_num + 1
    if line_num > 7 and line_num < len1 - 3:
        #print(line)
        size = line.split(" ")[-2]
        filename = line.split(" ")[-1].strip()
        #print(size)
        #print(filename)
        d[filename]=size
print(d)
print("Total bytes = ",sum(d.values()))
