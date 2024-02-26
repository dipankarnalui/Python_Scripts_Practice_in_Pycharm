#write a code to test if a number is palindrome or not 
inp="12321"
len=len(inp)
new = ""
while len > 0:
    #print(len)
    len = len - 1
    new=new + inp[len]

if new == inp:
    print("palindrome")
else:
    print("not palindrome")

