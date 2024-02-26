n=int(input("Enter the number: "))
print(n)
fact=n
while n > 1:
    #print(n)
    fact=fact * (n -1)
    #print("Fact= ", fact)
    n=n-1
print("Fact= ", fact)

