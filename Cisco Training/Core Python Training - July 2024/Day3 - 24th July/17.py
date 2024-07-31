'''
Enter the file name : one.txt
File status = file found
display all the words starting with "a"

contents of one.txt
-------------------
'''
f1 = open("one.txt", "w")
f1.write('''this is also an very ample 
data and very available
then end of this''')
f1.close()

#also
#an
#ample
#and
#available

fname=input("Enter the filename : ")
try:
    fob=open(fname,"r")
    for e in fob:
        line=e.rstrip("\n")
        word_list=line.split()
        for word in word_list:
            if word.startswith("a"):
                print(word)
except:
    print("file status = file not found")
finally:
    if fob:
        fob.close()



