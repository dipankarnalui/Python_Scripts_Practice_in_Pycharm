arr = [50,30,20,10,40,"arun","hello",60,"world"]
arr.sort(key=ascii)
f1 = open("data1.txt", "w")
for elem in arr:
  f1.write(str(elem)+"\n")
f1.close()
f1 = open("data1.txt", "r")
res = f1.read()
print(res)
f1.close()