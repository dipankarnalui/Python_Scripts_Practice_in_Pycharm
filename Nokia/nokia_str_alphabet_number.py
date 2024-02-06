#find the num of occurence of special symbols
#not alpha numeric
str = "{[([])]}an123[]0"
l1=[]
for ele in str:
    if not ele.isalnum() and ele not in l1:
        print(ele, str.count(ele))
        l1.append(ele)
