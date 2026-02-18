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
2609 -> 26.9
26.13 -> invalid
2607 -> 26.7 
26A7 -> invalid
'''


l1=['25121','23122','231214','2603','2609','26.13','2607','26A7']
for s in l1:
    print("processing => ", s)
    if s.isalnum():
        print("invalid")
    else:
        if "." in s:
            y,m=s.split(".")
            if int(m) > 12 :
                print("invalid")
        else:
            l=len(s)
            if l==5 or l==6:
                y,m,x=s[0:2],s[2:4],s[4:]
                if len(m) == 2 and int(m[0])== 0 :
                    m=m[1]
                if int(m) > 12 or int(x)>30 :
                    print("invalid")
                if len(x) == 2 and int(x[0])== 0 :
                    x=x[1]
                print(y+"."+m+"."+x)

            elif l == 4:
                y = s[0:2]
                m = s[2:4]
                if m.isdigit() and int(m) > 12:
                    print("invalid")
                else:
                    if len(m) == 2 and int(m[0]) == 0:
                        m = m[1]
                    print(y + "." + m)
            else:
                print("invalid")






