next_line_count=2
flag=False
count = 0
data=""
with open("input.txt", "r") as f:
    all_lines = f.readlines()
    for line in all_lines:
        if "neighbors:" in line:
            #print(line)
            flag=True
        if flag and count <= next_line_count:
            data = data + line
            count=count+1
#print(data)
print(data.splitlines())

'''        
words1=line1.split()
words2=line2.split()
d1={}
for i in range(len(words1)):
    d1[words1[i]]=words2[i]
print(d1)
'''





