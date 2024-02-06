#C=5(F-32)/9
farenhite=[102.56, 97.7, 99.14, 100.04]
celcius=[]
for f in farenhite:
    c=float(5 * (f - 32)/9)
    celcius.append(c)
print(celcius)

#------------List Comprehension----------->
celcius2 = [ float(5 * (f - 32)/9) for f in farenhite]
print(celcius2)
