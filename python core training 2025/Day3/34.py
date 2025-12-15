def square_lst(alst,blst):
    for i in range(len(alst)):
        blst[i]=alst[i] ** 2
    return blst
    
alst = [1,2,3,4,5]
blst = [0,0,0,0,0]

blst=square_lst(alst,blst)

print(alst)  # [1,2,3,4,5]
print(blst)  # [1,4,9,16,25]

