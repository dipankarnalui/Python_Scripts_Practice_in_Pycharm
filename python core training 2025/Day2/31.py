'''
Shallow copy:-
==============

Guess:-
-------
alst = [10,20,30,40,50,60]
blst = alst
alst[0] = 0
alst[1] = 0
alst[2] = 0
print(blst) # what will be output of this print statement ?

A) [10,20,30,40,50,60]
B) [40,50,60]
C) [10,20,30]
D) [0,0,0,40,50,60]

alst = blst         # shallow copy ( SHARING )

import copy
alst = copy.deepcopy(blst) # deep copy
                    # suitable nested data structure

Guess:-
-------
import copy

alst = [10,20,30,40,50,60]

blst = copy.deepcopy(alst)

alst[0] = 0
alst[1] = 0
alst[2] = 0

print(blst) # what will be output of this print statement ?
'''
