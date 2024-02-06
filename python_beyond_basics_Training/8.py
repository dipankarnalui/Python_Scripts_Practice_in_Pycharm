# 6) File Iterator:-
# ====================
# open the file in read mode  - fob is fileobject
f1 = open("one.txt", "w")
f1.write("hari\n")
f1.write("arun\n")
f1.write("manu\n")
f1.write("manoj")
f1.close()
fob = open("one.txt", "r")
for elem in fob:
   print(elem)
fob.close()