# import os
# fname=input("Enter the file name: ")
# if os.path.isfile(fname):
#     print("File status = file found")
#     fob=open(fname,"r")
#     for ele in fob:
#         ele=ele.rstrip("\n")
#         words=ele.split(" ")
#         for word in words:
#             if word.startswith("a") or word.startswith("A"):
#                 print(word)
# else:
#     print("File status = file not found")




fname=input("Enter the file name: ")
try:
    print("File status = file found")
    fob=open(fname,"r")
    for ele in fob:
        ele=ele.rstrip("\n")
        words=ele.split(" ")
        for word in words:
            if word.startswith("a") or word.startswith("A"):
                print(word)
except FileNotFoundError as e1:
    print(e1)
else:
    if fname:
        fname.close()