#Demo on tuple slicing:-
#=======================
# remove 30 from the tuple 

      # 0  1  2  3  4  5
data = (10,20,30,40,50,60)

index = data.index(30)  # first occurance of 30

before30 = data[0:index]     # data[0:2] --> (10,20)
after30  = data[index+1:]    # data[3:]  --> (40,50,60)
res = before30+after30       # (10,20) + (40,50,60)
print(res)


