arr = [10,20,30,40]
ctab = {"blr":5, "chn":6, "tpuram":7, "hyd":8, "mum":9}

index = int(input("Enter the index : "))
key   = input("Enter city name : ")

res = arr[index] + ctab[key]

print("RESULT = ",res)
print("Cleanup Activity")


#input : 0  blr    output ?
#input : 20 blr    output ?
#input : 1  del    output ?
#input : ^D        output ?

