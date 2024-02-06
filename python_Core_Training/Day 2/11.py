# alst = [1,2,3,4,5]
# blst = [0,0,0,0,0]
# def square_lst(alst,blst):
#     for i in range(0,len(alst)):
#         r= alst[i] * alst[i]
#         blst[i]=r
# square_lst(alst,blst)
# print(alst)  # [1,2,3,4,5]
# print(blst)  # [1,4,9,16,25]

alst = [1,2,3,4,5]
blst = [0,0,0,0,0]
def square_lst(alst,blst):
    i=0
    for e in alst:
        blst[i]= e * e
        i = i + 1
square_lst(alst,blst)
print(alst)  # [1,2,3,4,5]
print(blst)  # [1,4,9,16,25]