'''
*a,b,c = 10,20,30,40,50,60  #
a,*b,c = 10,20,30,40,50,60  #
a,b,*c = 10,20,30,40,50,60  #
*a,b,c = 10,20,30           #
*a,b,c = 10,20              #
*a,*b,c = 10,20,30          # Error
'''
alst = [
        "ravi-blr",
        "hari-chn",
        "manu-mum",
        "guru-del"
       ]
# define a empty list
newlst = []
n2=[]
# traverse on the list
for record in alst:
    # split the data based on the delimiter
    name, city = record.split("-")

    # collect the data
    newlst.append(city)
    n2.append(name)
# outside the for - print it
print(newlst)  # ["blr","chn","mum","del"]
print(n2)