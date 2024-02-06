#prime number can be divided by 1 and that number only
#prime number can not be divided by any other number
#Divide N by loop (2 to N-1)

def check_prime(n):
    prime=True
    if n == 1:
        print("prime")
    elif n>1:
        for i in range(2, n):
            print("i = ",i)
            div_res=n/i
            print("div res = ",div_res)
            after_point = str(div_res).split(".")[1]
            print("after point = ", after_point)
            if int(after_point) == 0:
                print("{} is fully divisible by {}. Hence {} is not prime.".format(n,i,n))
                prime=False
                break
            print("-------------------")
    return prime

n=int(input("Enter a Number: "))
res=check_prime(n)
if res is False:
    print("Not prime")
else:
    print("prime")
