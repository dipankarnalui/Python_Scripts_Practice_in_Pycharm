#Reverse string using backward for loop
inp="PythoN"
len=len(inp)
s3=''
while len != 0:
    len=len-1
    s3 = s3 + inp[len]
print(s3)

