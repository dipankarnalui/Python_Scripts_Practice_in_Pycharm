name="manoj"

#convert 1st letter to upper case
print(name[0].upper() + name[1:])

#convert last letter to upper case
print(name[0:-1] + name[-1].upper())
print(name[:-1] + name[-1].upper()) #no need to write default 0

#convert 1st and last letter to upper case
print(name[0].upper() + name[1:-1] + name[-1].upper())