data1 = "ravi,JOHN,umesh,Deepak,Anit"
data2 = "aditya,Avinash,Ravi,DEEPAK"
d1=set(data1.lower().split(","))
d2=set(data2.lower().split(","))
print(d1.intersection(d2))
print(d1 & d2)

print(d1 | d2)
'''
Expected:-
----------
common names b/w two datas are
{"ravi", "deepak"}
Duration : 10 mins
Time     : 2.55 to 3.05
hint:  convert to lower case
       split them based on a delimiter - split()
       convert the list into a set
       use intersection to find the common elements
'''