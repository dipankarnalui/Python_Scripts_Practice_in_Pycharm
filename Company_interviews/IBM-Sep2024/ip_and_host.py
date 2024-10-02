d1={}
d2={}
with open("input.txt", "r") as f:
    all_lines=f.readlines()
    for line in all_lines:
        if "." in line.strip():
            first=line.split()[0]
            hostname=line.split()[1]
            if first.count(".") == 3:
                d1[first]=hostname
        if ":" in line.strip():
            if line.startswith("f"):
                first = line.split()[0]
                sec=line.split()[1]
                d2[first] = sec
print(d1)
print(d2)

