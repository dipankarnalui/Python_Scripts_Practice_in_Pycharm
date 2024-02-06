#American Megatrends Interview
#write a code to reverse the words in a sentence
s = "the sky is blue"
#output = "eht yks si eulb"

l1=s.split()
#print(l1)
output=""
for e in l1:
    output= output + " " + e[::-1]
print(output)    