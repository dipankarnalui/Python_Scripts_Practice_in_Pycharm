'''
input=
25121
23122
231214
2603
2609
'''

'''
Output

YY.MM.X
YY.MM.X
YY.MM
YY.M

25121 -> 25.12.1
23122 -> 23.12.2
231214 -> 23.12.14
2603 -> 26.3
2607 -> 26.7
2609 -> 26.9
26.13 -> invalid
26A7 -> invalid
26.A7 -> invalid
'''

def generate_sprint(y,m,x):
    if len(m) > 0:
        if int(m) > 12:
            print(f"{s} is invalid as month greater than 12")
        if int(m[0]) == 0:
            m = m[1]
    if len(x) > 0:
        if int(x) > 30:
            print(f"{s} is invalid as day greater than 30")
        if int(x[0]) == 0:
            x = x[1]
    return y,m,x

l1 = ['25121', '23122', '231214', '2603', '2609', '26.13', '2607', '26A7','26.A7']
for s in l1:
    if 'A' in s:
        print(f"{s} is invalid as it contains A")
        continue
    elif "." in s:
        y, m, *x = s.split(".")
    else:
        y, m, x = s[0:2], s[2:4], s[4:]
    y,m,x = generate_sprint(y,m,x)
    print(y+"."+m+"."+str(x))





