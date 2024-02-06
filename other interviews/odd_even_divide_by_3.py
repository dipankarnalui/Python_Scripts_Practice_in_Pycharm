#print all the odd numbers from 50 to 100
#from those numbers print only which are devided by 3
#count how many numbers
odd=[]
even=[]
start,end=50,101
for i in range(start,end):
    if i % 2 != 1:
        even.append(i)
    else:
        odd.append(i)
print("odd = ",odd)
print("even = ", even)
div3=[]
for element in odd:
    if element % 3 == 0:
        div3.append(element)

print("Divided by 3 = ", div3)
print("Total elements = ",len(div3))