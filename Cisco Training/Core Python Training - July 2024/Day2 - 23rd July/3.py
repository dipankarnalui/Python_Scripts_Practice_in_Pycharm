age = int(input("Enter your age: "))
if age >= 18 :
    print("Eligible to vote")
else:
    print("Not Eligible to vote")



value = int(input("Enter a value : "))
if value>=10 and value<=20:
    print("GRP-1")
elif value>20 and value<=30:
    print("GRP-2")
else:
    print("GRP-3")

sent = "learning python is easy"
word = input("Enter a word : ").lower()
if word in sent:
    print("given word is part of sentence")
else:
    print("given word not a part of sent")