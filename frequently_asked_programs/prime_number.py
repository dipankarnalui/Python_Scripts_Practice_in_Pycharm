'''
A prime number is a whole number greater than 1 that can be divided evenly by **only two numbers: 1 and itself

For example:

So the first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

'''

n=int(input("Enter the number : "))
print(f"Checking number {n}")
prime=True
if n<2:
    prime=False
else:
    for i in range(2,n):
        print(f"{n}%{i}={n%i}")
        if n%i==0:
            prime=False
            break
print(F"Prime = {prime}")