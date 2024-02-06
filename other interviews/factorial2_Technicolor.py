n=int(input("Enter the number: "))

def f(n):
    print(n)
    if n != 1:
        fact = n * f(n-1)
        n=n-1
        return fact
    else:
        return 1
print(f(n))
