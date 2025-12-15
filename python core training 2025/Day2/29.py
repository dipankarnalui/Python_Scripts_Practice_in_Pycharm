# Problem Statement :
# from the given list - 
# delete all the occurances of a given number

alst = [10,40,30,10,20,10,50,10,10,20,40,10]

# assume we have to remove all the occurances of 10

# find the no of occurances
cnt = alst.count(10)

# loop for 6 times i.e count no of times
for _ in range(cnt):
    alst.remove(10)

print(alst)