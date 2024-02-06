'''
Task:-
======
Given:-
-------
'''
alst = [1,2,3,4,5]
'''
Expected:-
----------
newlst = [1,4,9,16,25]
Duration : 10 mins
Time     : 12.35 to 12.45
Hint     : newlst.append(1)
Input data is in "alst"
output data is in "newlst"
is it In-place/Out-place ? 
using appor iterator & gets the things done 
'''
'''
alst = [1,2,3,4,5]
new=[]
for i,v in enumerate(alst):
    print(i,v)
    #new[i] = v * v
print(new)
###---wrong implementation.... two list..not same list...use forward iterator 
alst = [1,2,3,4,5]
new=[]
for i in range(0,len(alst)):
    r = alst[i] * alst[i]
    new.append(r)
print(new)
'''

alst = [1,2,3,4,5]
#newlst [1,4,9,16,25]
newlst =[]
for elem in alst:
    newlst.append(elem*elem)
print(newlst)