#The lowest grade 36 of  belongs to Tina.
# The second lowest 37 grade of  belongs to both Harry and Berry,
# so we order their names alphabetically and print each name on a new line.

students = [['Harry', 37], ['Berry', 37], ['Tina', 36], ['Akriti', 36], ['Harsh', 39]]
d1=dict(students)
values = []
for key,value in d1.items():
    values.append(value)
min_value=min(values)
#print("min value = ", min_value)
delete_keys = []
count=0
for key,value in d1.items():
    if value == min_value:
        delete_keys.append(key)
        count = count + 1
#print("Before delete = ", d1)
for key in delete_keys:
    del d1[key]
#print("After delete = ", d1)
values=[]
for key, value in d1.items():
    values.append(value)
min_value=min(values)
keys=[]
for key, value in d1.items():
    if value == min_value:
        keys.append(key)
keys.sort()
for key in keys:
    print(key)