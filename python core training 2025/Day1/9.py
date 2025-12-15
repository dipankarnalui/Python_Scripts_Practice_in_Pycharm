name = "arvindhan"
res1 = name[:2].upper() + name[2:-2] + name[-2:].upper()
res2 = name[:4].upper() + "-" + name[4:]
res3 = name[:4].upper() + "-" + name[4:].upper()[::-1]

print(res1)
print(res2)
print(res3)