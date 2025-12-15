def classify(numlst): 
    oddlst,evenlst = [],[]
    for elem in numlst:
        if elem%2==0:
           evenlst.append(elem)
        else:
           oddlst.append(elem)

    return evenlst,oddlst

res=classify([1,2,3,4,5,6])
print(res)
print(res[0]) # [2,4,6]
print(res[1]) # [1,3,5]

'''
1) function name    - classify
2) how many args    - 1
3) datatype of args - list
4) type of function - positional
5) does it return ? - yes
6) is it a pure fn? - yes
7) local vars       - numlst,oddlst,evenlst,elem
8) how to call      - res=classify([1,2,3,4,5,6])
                      print(res[0]) # [2,4,6]
                      print(res[1]) # [1,3,5]

'''