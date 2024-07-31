f1 = open("data.txt", "w")

f1.write("arun=10\n")
f1.write("manu=20\n")
f1.write("ravi=30\n")
f1.write("john=40\n")
f1.write("basu=50")

f1.close()

f1 = open("data.txt", "r")

print(f1.read())

f1.close()
