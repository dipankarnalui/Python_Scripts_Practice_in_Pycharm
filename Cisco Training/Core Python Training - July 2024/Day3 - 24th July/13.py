fob = open("data.txt", "r")

for elem in fob:
    elem = elem.rstrip("\n") # remove the \n from elem
    print(elem.split("=")[0])

fob.close()
