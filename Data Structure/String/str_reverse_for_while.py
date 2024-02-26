#Reverse string using backward for loop
inp="PythoN is EasY"
print("input = {} ".format(inp))
len=len(inp)

store1=''
#backward for loop using reversed
#start value will be smaller than end value
for i in reversed(range(0,len)):
    #print(i)
    store1 = store1 + inp[i]
print("output 1 = {} ".format(store1))

store2=''
#for loop to traverse backward by step using -1, -2, +1, +2 etc..
for i in range(len-1,-1,-1):
    #print(i)
    store2 = store2 + inp[i]
print("output 2 = {} ".format(store2))


store3=''
#instead of using for loop, we can use while loop to traverse backward
while len != 0:
    #print(len)
    len=len-1
    store3 = store3 + inp[len]
print("output 3 = {} ".format(store3))
