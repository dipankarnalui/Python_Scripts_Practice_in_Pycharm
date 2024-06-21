num=12121
store=""
for i in range(len(str(num))-1,-1,-1):
    #print(str(num)[i],end="")
    store = store + str(num)[i]
if int(store) == num:
    print("palindrome")
else:
    print("not palindrome")