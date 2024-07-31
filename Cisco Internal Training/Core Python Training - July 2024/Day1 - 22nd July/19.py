name="arvindhan"

#ARvindhAN
#1st 2 and last 2 letters upper case
print(name[0:2].upper() + name[2:-2] + name[-2:].upper())
print(name[:2].upper() + name[2:-2] + name[-2:].upper())

#ARVI-ndhan
#1st 4 upper then concatenate hyphen
print(name[0:4].upper() + "-" + name[4:])
print(name[:4].upper() + "-" + name[4:])

#ARVI-NAHDN
#all letter upper case
#1st 4 + hyphen and reverse of remaining
print(name[0:4].upper() + "-" + name[-1:3:-1].upper())
print(name[0:4].upper() + "-" + name[4:].upper()[::-1])
print(name[:4].upper() + "-" + name[4:].upper()[::-1])


