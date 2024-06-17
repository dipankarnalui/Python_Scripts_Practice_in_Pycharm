num=int(input("Enter a number : "))
prime=True
for i in range(2,num):
    if num%i == 0:
        prime=False
        break
    else:
        continue
if prime==True:
    print("prime")
else:
    print("not prime")