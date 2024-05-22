#Find anagram

str1="abc"
#str2="bacd"
str2="bac"

if len(str1) == len(str2):
    for i in range(len(str1)):
        if str1[i] in str2:
            if str1.count(str1[i]) == str2.count(str1[i]):
                print(str1[i] + " is in " + str2)
        else:
            print("not anagram")
else:
    print("not anagram")