a1=["a","b","c","d","e","f","g"]
for i in range(len(a1)):
    print(i,a1[i])

print("zip --------")
b1=["a","b","c","d","e","f","g"]
for a,b in zip(a1,b1):
    print(a,b)

print(list(zip(a1,b1)))