filepath= "file.log"
filepath2="error_file.log"
with open(filepath,"r") as f:
    all_lines=f.read()
    for line in all_lines.splitlines():
        if line.startswith("Error"):
            with open(filepath2,"a") as f2:
                f2.write(line + "\n")
count=0
l1=[]
with open(filepath2,"r") as f:
    all_lines = f.read()
    for line in all_lines.splitlines():
        count=count+1
        code=line.split(" ")[1]
        l1.append(code)
print("Total Error count = ", count)
print(l1)
for e in l1:
    print("Error code {} is present {} many times.".format(e,l1.count(e)))

