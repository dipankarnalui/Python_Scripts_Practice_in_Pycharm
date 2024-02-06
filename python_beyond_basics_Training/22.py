'''
Demo-
=====
Given:
------
  alst = [10,20,30,40,50]
  blst = [1,2,3,4,5]
Expected:
---------
  newlst = [11,22,33,44,55]
hint: outputlst = list(map(?, alst,blst))
solution:-
----------
alst = [10,20,30,40,50]
blst = [1,2,3,4,5]
newlst = list(map(lambda x,y : x+y, alst,blst))
#OR
newlst = list(map(lambda x : x[0]+x[1], zip(alst,blst)))
print(newlst)
'''