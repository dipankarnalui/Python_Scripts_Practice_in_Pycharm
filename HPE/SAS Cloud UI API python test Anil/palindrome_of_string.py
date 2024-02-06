#string palindrome
s="abcbab"
print("input = ",s)
s1=""
ln=len(s) #
for i in range(ln-1,-1,-1):
    s1= s1 + str(s[i])
print("after reverse = ", s1)
if s == s1 :
    print("Palindrome")
else:
    print("NOT Palindrome")