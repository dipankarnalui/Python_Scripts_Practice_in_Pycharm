#Program to check a number is palindrome or not without help of a string/list in Python

#num=4567654
num=456765483
check_num = num
print("num = ",num)
palindrome=0
while num!=0:
    ln = len(str(num))
    print("len = ",ln)
    last=num%10
    remaining=num//10
    num=remaining
    print("last = ", last)
    print("remaining = ", remaining)
    palindrome = palindrome + (last * (10**(ln-1)))
    print("palindrome = ",palindrome)
    print("------------------")
if palindrome == check_num:
    print("{} is a palindrome number".format(check_num))
else:
    print("{} is not a palindrome number".format(check_num))
