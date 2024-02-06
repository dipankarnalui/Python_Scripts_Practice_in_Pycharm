separator="."
s2="world"
s3=separator.join(s2)
print(separator)
print(s2)
print(s3)

#write a program to check if a string is palindrome or not
s1="abcba"
s2=""
for e in s1:
    s2=e+s2
print(s2)
if s1 == s2 :
    print("palindrome")
else:
    print("not palindrome")
