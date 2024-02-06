# f1 = open("data.txt", "w")
# f1.write("arun=10\n")
# f1.write("manu=20\n")
# f1.write("ravi=30\n")
# f1.write("john=40\n")
# f1.write("basu=50")
# f1.close()
'''
>> python "\n" is read as it is - no conversion
>> "\n" is a part every line we read from the file
>> it is programmers choice to handle "\n"
   can be retained or deleted
'''
fob = open("data.txt", "r")
for elem in fob:
    #print(elem)
    elem = elem.rstrip("\n")   # we are deleting \n
    #print(elem)
    print(elem.split("=")[0])
fob.close()
