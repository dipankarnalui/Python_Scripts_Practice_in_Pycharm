string1="0T1h2i3s4 5i6s 7a"
len1=len(string1)
print("string length =",len1)
'''
#forward loop==>
for i in range(0, len1):
    print(string1[i])
'''
#backward loop==>
for i in range(len1 - 1, -1, -1):
    print(string1[i])