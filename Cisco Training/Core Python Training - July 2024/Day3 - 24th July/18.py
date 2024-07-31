arr = [50,30,20,10,40,"arun","hello",60,"world"]

res = []

for elem in arr:
    if type(elem)==int:
        res.append(elem)

res.sort()

f1 = open("arr.txt", "w")
f1.write("\n".join(str(e) for e in res))
f1.close()

f1 = open("arr.txt", "r")
print(f1.read())
f1.close()

