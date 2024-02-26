input="15637 498590 hshkjd 9836328472  !@#&$^^#"
len1=len(input)
str1=""
for i in range(len1-1, -1, -1):
    str1 = str1 + str(input[i])
print(str1)

#TC -- numeric,#$#@
#TC -- space
#limit -len - 10000
#0 char

