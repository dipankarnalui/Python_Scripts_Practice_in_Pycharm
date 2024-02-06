#for mac/linux/unix users:-
import subprocess
output = subprocess.check_output("ls -l", shell=True).decode("utf-8")
output = output.split("\n")[1:-1]
filedict = {}
for line in output:
    flst  = line.split()
    print(flst)
    if flst[0][0]=="-":
        name = flst[-1]
        size = flst[4]
        filedict[name] = size
print(filedict)