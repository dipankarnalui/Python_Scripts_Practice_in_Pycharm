#str=”abcdabcaaa”
#find out  count of unique 3 char cont. Substring in this original string .
#“abc , bcd , cda , dab , bca, caa, aaa “
#Ans=  7

inp="abcdabcaaa"
list1=list(inp)
l=len(list1)
tmp=[]
for i in range(0,l-2):
    char=str(list1[i]) + str(list1[i + 1]) + str(list1[i + 2])
    tmp.append(char)
print(set(tmp))






