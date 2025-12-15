filename = input("Enter the filename : ")

f1=None
try:
    f1 = open(filename, "r")

    for line in f1:
        wordlst = line.split()
        for word in wordlst:
            if word[0]=="a":   # if word.startswith("a")
               print(word)

except FileNotFoundError as e1:
    print("File Not Found")
finally:
    if f1:
       f1.close()
