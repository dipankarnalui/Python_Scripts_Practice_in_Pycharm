##prime number = 2,3,5,7,11,13,17,19
num=9
prime=True
for i in range(2,num):
    print("division = ",num/i)
    print("remainder = ",num%i)
    if num%i == 0:
        print("{} is divisible by {}".format(num,i))
        prime=False
        break
    else:
        prime=True
if prime:
    print("prime")
else:
    print("not prime")