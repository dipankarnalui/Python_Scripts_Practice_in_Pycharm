sentence="aWESOME is cODING"
#print("input sentence= ", sentence)
tmp=[]
for word in sentence.split(' '):
    tmp.append(word)
len_tmp=len(tmp)
#print("total elements = ", len_tmp)

'''
rev_list=[]
for index in range(1,len_tmp+1):
    #print(-index, tmp[-index])
    rev_list.append(tmp[-index])

print(' '.join(rev_list))
'''

rev_list=reversed(tmp)
rev_str=' '.join(rev_list)
print("Reversed sentence = ",rev_str)

rev_list_new=list(rev_str)
rev_case_list=[]
for index in range(0,len(rev_list_new)):
    ele=str(rev_list_new[index])
    #print("element is = ",ele)
    if ele.isupper():
        item=ele.lower()
        #print("ele is changed to lower = ", item)
    elif ele.islower():
        item=ele.upper()
        #print("ele is changed to upper = ", item)
    else:
        item=ele
        #print("ele is not changed = ", item)
    rev_case_list.append(item)

case_rev_string=''.join(rev_case_list)
#print("Case Reversed string = ",case_rev_string)


'''
final_string=""
for ele in tmp:
    final_string=final_string+ " " + ele
print("Output = ",final_string.strip())
'''
