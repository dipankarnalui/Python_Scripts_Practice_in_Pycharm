str1="awbfbcdeabcdebcdfbcdewvfdgbcdetdhfg"
str2="bcde"
while str2 in str1:
    position=str1.index(str2)
    print("position of '" + str2 + "' in str1 = ", position)
    str1 = str1[:position] + "0000" + str1[position+4:]
    print(str1)
