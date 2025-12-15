res1 = "Manoj"  # convert first letter to upper case
res2 = "manoJ"  # convert last letter to upper case
res3 = "ManoJ"  # convert first & last letter to uppercase

name = "manoj"


name = input("Enter u r string : ")

res1 = name[0].upper() + name[1:]
res2 = name[:-1] + name[-1].upper()
res3 = name[0].upper() + name[1:-1] +  name[-1].upper()

print(res1)
print(res2)
print(res3)