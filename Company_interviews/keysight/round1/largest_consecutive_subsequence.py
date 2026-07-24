#Find the largest consecutive (subsequence) length for any character in the string

input = "aaaabbbabccddddda"

#output:
#a:3
#b:3

d1={}
count=1
for i in range(len(input)-1):
    #print(input[i], input[i+1])
    if input[i] == input[i+1]:
        count = count + 1
        d1[input[i]]=count
        print(d1)
        print(count)
    else:
        print("mismatch")
        count=1
        print(count)
print(d1)