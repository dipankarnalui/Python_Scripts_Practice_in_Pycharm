def append_item(item, bucket=[]):
   bucket.append(item)
   print(id(bucket))
   return bucket

print(append_item(1))
print(append_item(2))
print(append_item(3, []))
print(append_item(4))
