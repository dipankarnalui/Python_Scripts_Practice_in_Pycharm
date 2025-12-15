f1 = open("task1.txt", "w")
f1.write("north-del-10\n")
f1.write("south-blr-20\n")
f1.write("west-mum-30\n")
f1.write("east-kol-40")
f1.close()

# verify 
f1 = open("task1.txt", "r")
#print(f1.read())
#f1.close()

# start writing the code here
res1=[]
res2=[]
res3={}
for line in f1:
    side,city,price=line.rstrip("\n").split("-")
    res1.append(int(price))
    res2.append(city)
    res3[side]=city
print(res1)
print(res2)
print(res3)

'''
Expected:-
-----------
print(res1) # [10,20,30,40]
print(res2) # ["del","blr","mum","kol"]
print(res3) # {
               "north" : "del", 
               "south" : "blr", 
               "west"  : "mum", 
               "east"  : "kol"
              }

'''