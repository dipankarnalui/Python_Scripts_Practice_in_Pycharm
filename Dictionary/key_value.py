"""
A, 34 78 96
B, 23 94 62
C, 19 83 30
{'A': ' 34 78 96', 'B': ' 23 94 62', 'C': ' 19 83 30'}
 34 78 96
 23 94 62
 19 83 30
"""
len=3
dict1={}
for i in range(0,3):
    key, value = input().split(",")
    dict1[key]=value
print(dict1)
for key in dict1.keys():
    print(dict1[key])