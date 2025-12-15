fob = open("data.txt", "r") 

for elem in fob:
    elem = elem.rstrip("\n")   # remove the \n from elem
    print(elem.split("=")[0])

fob.close()

'''
data.txt
---------
               elem              elem.rstrip("\n") elem.split("=")     
"arun=10\n"  1)elem="arun=10\n"  elem="arun=10"    ["arun","10"]
"manu=20\n"  2)elem="manu=20\n"  elem="manu=20"    ["manu","20"]
"ravi=30\n"  3)elem="ravi=30\n"  elem="ravi=30"    ["ravi","30"]
"john=40\n"  4)elem="john=40\n"  elem="john=40"    ["john","40"]
"basu=50"    5)elem="basu=50"    elem="basu=50"    ["basu","50"]

Note:
  -we can only write/read strings from a file
  -open the file for a particular purpose
'''
