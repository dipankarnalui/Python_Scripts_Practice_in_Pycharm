num=9
#identify prime or not
prime=True
for i in range(2,num):
    if num%i == 0:
        print("not prime")
        prime=False
        break
if prime:
    print("prime")

