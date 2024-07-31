f1 = open("task1.txt", "w")
f1.write("north-del-10\n")
f1.write("south-blr-20\n")
f1.write("west-mum-30\n")
f1.write("east-kol-40")
f1.close()
# start writing the code here
res1=[]
res2=[]
fob = open("task1.txt", "r")
for elem in fob:
    elem = elem.rstrip("\n") # remove the \n from elem
    loc,r1,r2=elem.split("-")
    res1.append(r1)
    res2.append(int(r2))
print(res1) # [10,20,30,40]
print(res2) # ["del","blr","mum","kol"]
fob.close()