x=[1,2,3,4,5]
#rotate element
#right shift
#1st=[5,1,2,3,4]
#2nd=[4,5,1,2,3]
#3=[3,4,5,1,2]
#4=[2,3,4,5,1]
#5=[1,2,3,4,5]

y=[]
l=len(x)
'''
for i in range(l-1,-1,-1):
    y.append(x[i])
    print(y)
'''
for i in range(l-1,-1,-1):
    #right shift
    print(x)     