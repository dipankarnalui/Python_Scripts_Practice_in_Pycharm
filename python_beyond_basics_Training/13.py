'''
Dictionary:-
=============
>> collection of key-value pairs
>> key should be Im-mutable
>> value can be im-mutable/mutable
'''
months = {
           "jan" : 1,       # "jan" is a key and 1 is a the value
           "feb" : 2,
           "mar" : 3,
           "apr" : 4
         }
user = input("Enter a month : ").lower()
if user in months:  # Search for user input in the months dict
   print("Found")
   print("Value = ",months[user])
else:
   print("NOT FOUND")
'''
Applications:-
==============
>> design a lookup table
>> frequency count
>> sub-total
>> sub-grouping
'''