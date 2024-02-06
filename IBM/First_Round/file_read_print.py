# read file and print the file content
d1={}
with open("simple.txt", "r") as f:
    #all_lines=f.readlines()
    all_lines = f.read().splitlines() #to remove /n
    for line in all_lines:
        if line.startswith("IP"):
            k=line.split("=")[0]
            v=line.split("=")[1]
            d1[k]=v
#print(d1)
for key,val in d1.items():
    print(key + " : " + val)