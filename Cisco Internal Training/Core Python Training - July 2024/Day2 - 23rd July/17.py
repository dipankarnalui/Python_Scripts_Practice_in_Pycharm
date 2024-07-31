#tupple example
#no change
weeks=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
#without bracket also works
weeks="Sun","Mon","Tue","Wed","Thu","Fri","Sat"
print(weeks[0])

months="jan","feb","mar","apr"
#months[0]="January"  #not write support in tupple

merge = weeks + months #operator overloading
print(merge)

if weeks==months: #operator overloading
    print("same content")
else:
    print("two diff tupple")

#slice
print(weeks[-3:])
print(months[1:])

