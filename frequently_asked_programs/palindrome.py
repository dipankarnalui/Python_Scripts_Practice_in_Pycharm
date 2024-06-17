word1="abcba"
word2=""
for i in range(len(word1)-1,-1,-1):
    print(word1[i], end="")
    word2=word2 + word1[i]
print(" ")
if word1 == word2:
    print("Palindrome")
