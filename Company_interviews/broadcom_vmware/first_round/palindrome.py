str1 = "abcban"
store = ""
for i in range(len(str1) - 1, -1, -1):
    store = store + str1[i]
print("after reverse = ",store)
if str1 == store:
    print("palindrome")
else:
    print("not palindrome")

