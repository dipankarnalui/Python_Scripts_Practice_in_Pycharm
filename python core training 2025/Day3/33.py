#Call by VALUE :-
#=================
def fun(alst):
   alst[0:3] = [0]*3
   

numlst = [1,2,3,4,5,6]
print(numlst)    # [1,2,3,4,5,6]
fun(numlst.copy())
print(numlst)    # [1,2,3,4,5,6]


