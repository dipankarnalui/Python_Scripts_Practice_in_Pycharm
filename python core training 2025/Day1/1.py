import sys

num = 10
print("Value     = ",num)                    #-  10
print("Data Type = ",type(num))              #-  class int
print("Ref count = ",sys.getrefcount(num))   #-  actual + 1
print("Unique ID = ",id(num))                #-  69762504 
print("Size in memory = ",sys.getsizeof(num)) # 28
print("Size in memory = ",num.__sizeof__())   # 28

