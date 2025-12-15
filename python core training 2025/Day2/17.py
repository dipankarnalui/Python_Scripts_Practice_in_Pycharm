# Mutable List

#       0  1  2  3  4
alst = [10,20,30,40,50]

             #[0,1,2,3,4]
for index in range(0,len(alst),1):
    alst[index] = alst[index] + 1


print(alst)

