def insert_zero(alst,num):
    blst = []
    for ele in alst:
        blst.append(ele)
        blst.append(0)
    return blst
alst = [10,15,20,18,16]
res = insert_zero(alst,0)
print(res)  #[10,0,15,0,20,0,18,0,16,0]
'''
Duration: 10 mins
Time    : 3.12 to 3.22
1) function name     -  insert_zero
2) how many args     -  2
3) data type of args - list,int
4) type of function  - positional/compulsory
5) does it return    - yes
6) is it a pure fn?  - yes
7) local vars        - alst,blst,ele
8) how to call       - res = insert_zero(alst,0)

'''