dob = "15-aug-1947"

flst = dob.split("-")  # SPLIT returns a LIST

# split first argument is a DELIMITER
# split returns a LIST
                      
                  # flst[0]  flst[1]  flst[2]   
print(flst)       # ["15" ,  "aug",   "1947"  ]
#                    flst[-3] flst[-2] flst[-1] 

print(flst[0])    # 15
print(flst[1])    # aug
print(flst[2])    # 1947
print(flst[-1])   # 1947


print(flst[2][-1])   #  7 
print(flst[-2][0])   #  a
print(flst[0][0])    #  1
print(flst[-1][-1])  #  7
print(flst[1][:2])   #  au
print(flst[2][-2:])  #  47
print(flst[-1][:2])  #  19
print(flst[1][1:-1]) #  u
print(flst[2][1:-1]) #  94
