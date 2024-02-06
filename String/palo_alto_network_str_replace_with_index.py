str1="awbfbcdeabcdebcdfbcde"
str2="bcde"
number_of_time = str1.count(str2)
print("number_of_time = ", number_of_time)
length=len(str2)
for i in range(0,number_of_time):
    if str2 in str1:
        index=str1.index(str2)
        print("index of str2 in str1 = ", index)
        str1 = str1[:index] + "0000" + str1[index+length:]
        print(str1)
    else:
        print("str2 not present in str1")