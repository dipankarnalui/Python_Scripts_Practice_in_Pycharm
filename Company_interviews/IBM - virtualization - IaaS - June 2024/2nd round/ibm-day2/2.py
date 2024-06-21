'''
multiple of 3
3,6,9,12,18
*,*,*
*,*,*,*,*,*
3x1=3 start
3x2=6
3x3=9
3x4=12
3x5=15
3x6=18
num=3x7=21 > (n=20) stop
'''
n=20
mul=3
num=0
count=0
while num<n and mul>1:
    count = count + 1
    num=mul*count
    if num>n:
        break
    for i in range(num):
        print("*", end=" ")
    print(" ")