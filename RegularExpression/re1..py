import re
with open("input.txt","r") as f:
    all_lines=f.readlines()
    for line in all_lines:
        #print(line)
        pattern="[a-f]"
        x = re.findall(pattern,line)
        print(x)