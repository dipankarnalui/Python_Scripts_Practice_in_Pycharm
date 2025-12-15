def insert_zero(alst,val):
    alst.append(val)
    return alst
alst = [10,15,20,18,16]
res = insert_zero(alst,0)
print(res)  #[10,0,15,0,20,0,18,0,16,0] 
res=insert_zero([1,2,3,4],0)
print(res)

'''

1) function name     -  insert_zero
2) how many args     -  2
3) data type of args -  list, int
4) type of function  -  positional args
5) does it return    -  yes
6) is it a pure fn?  -  yes
7) local vars        -  ?
8) how to call       -  res=insert_zero([1,2,3,4],0)
'''