numlst = ["10","50","blr","30","hari","arun","40","derrick","20"]

res = []
for elem in numlst:
    if elem.isdigit():
       res.append(int(elem)) # convert & store

print(res)
res.sort()
print(res)

  
#output      operation       input   condition 
#               3          1             2              
#res=sorted([int(e) for e in numlst if e.isdigit()])

