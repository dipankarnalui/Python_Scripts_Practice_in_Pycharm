#print the numeric only from the string
a="q2w3e4r5"

'''
res=0
for i in a:
    if i.isnumeric():
        res = res + int(i)
print(res)
'''
for i in a:
    if int(i) in range(0,9):
        print(i)