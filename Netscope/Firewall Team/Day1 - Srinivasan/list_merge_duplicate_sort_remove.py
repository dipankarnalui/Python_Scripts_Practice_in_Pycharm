A = ['1126', '1129', '1189', '1190', '1191', '1199', '2239', '3001', '3002', '3003', '3004', '3005', '4005', '3000']
B = ['100', '200', '1199', '3000']
Result = ['100', '200', '1126', '1129', '1189-1191', '1199', '2239', '3000-3005', '4005']
# Merge A & B
# Remove duplicates
# Sort it
# Will parse and find the continuous numbers and then store the first and last element as first-last format, ignore/remove the middle elements
# Result = ['100', '200', '1126', '1129', '1189-1191', '1199', '2239', '3000-3005', '4005']
#print("Before Merge")
#print("A = ", A)
#print("B = ",B)
A.extend(B)
#print("After merge A and B")
#print(A)
dup=[]
for i in range(len(A)):
    if A.count(A[i]) > 1 and A[i] not in dup:
        dup.append(A[i])
#print("Duplicate items: ")
#print(dup)
for e in A:
    if e in dup:
        #print("remove index = ", A.index(e))
        A.remove(A[A.index(e)])
#print("After removing Duplicate")
#print(A)
for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        if int(A[i]) > int(A[j]):
            A[i],A[j]=A[j],A[i]
print("After Sort")
print(A)
'''
def check_next_element_in_sequence(A,pos):
    if int(A[pos]) + 1 == int(A[pos+1]):
        return True
def replace(A,new_value,pos):
    A.insert(pos,new_value)
for e in A:
    pos=A.index(e)
    first=pos
    while check_next_element_in_sequence(A,pos):
        pos=pos+1
        last=pos
        new_value=A[first] + "-" + A[last]
        replace(A,new_value, A.index(A[first]))
        if pos > len(A):
            break
print(A)
'''

for e in A:
    #print("element = ",e)
    i=A.index(e)
    #print("index of the element = ",i)
    #print("len = ",len(A))
    if i < len(A) - 1:
        print("A[i] = {}, A[i+1] = {}".format(A[i],A[i+1]))
        if '-' in A[i-1]:
            print("previous element has - Hyphen")
            if int(A[i-1].split('-')[1]) + 1 == int(A[i]):
                A[i-1] = A[i-1].split('-')[0] + "-" + A[i]
                print("removed = ", A[i])
                A.remove(A[i])
                print("changed current element = ", A[i-1])
        elif int(A[i]) + 1 == int(A[i+1]):
            print("next element is consecutive")
            A[i]=A[i] + "-" + A[i+1]
            print("removed next element = ", A[i+1])
            A.remove(A[i+1])
            print("changed current element = ", A[i])
print("After removing continuous number")
print(A)