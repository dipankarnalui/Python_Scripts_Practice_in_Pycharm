#write a program to check if a string is palindrome or not
s1="abcba"
print("input string = ", s1)
s2=""
for e in s1:
    s2=e+s2
print("reversed string = ",s2)
if s1 == s2 :
    print("palindrome")
else:
    print("not palindrome")