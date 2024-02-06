list1=[1,4,6,8,2,90,34,56]
list2=[1,4,6,8,2,90,35,56]
#compare..eual or not...equal in len...content...
len1=len(list1)
len2=len(list2)
status=False
if len1 != len2 :
    print("lists are not identical")
else:
    print("Len is equal..will check content...")
    for i in range(0,len1):
        if list1[i] == list2[i]:
            status=True
        else:
            status=False
            print(list1[i])
            break

print(status)
if status:
    print("length and content are same in both the list")
else:
    print("length and content are NOT same in both the list")
