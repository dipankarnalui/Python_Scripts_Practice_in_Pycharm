#write a code to print the number of elements just after the elements
'''
I/P: aaabbc
O/P: a3b2c1
'''
input="aaabbc"
store=""
for i in input:
    if i not in store:
        store=store + str(i) + str(input.count(i))
print(store)

#input="aaabbca"
'''
aaaaaa
a
111
a@##$&*aa=+
@@@@
(a112aaa
 aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccccaaa
 '''