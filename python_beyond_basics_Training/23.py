alst = [3,5,2,6,7,12,16,10,11]
newlst = list(filter(lambda x : x%2==0, alst))
print(newlst)  # [2,6,12,16,10]