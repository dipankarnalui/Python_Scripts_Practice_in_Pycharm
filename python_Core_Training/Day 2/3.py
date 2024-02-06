number = 1453
#expected = one four five three
d1 = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
}

for e in str(number):
    if e in d1.keys():
        print(d1[e], end =" ")

#print(list(str(number)))