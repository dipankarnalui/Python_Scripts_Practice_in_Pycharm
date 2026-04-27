'''
You are given a JSON object that may contain nested objects and arrays.
Task is to print all keys with full paths and their values in a flattened format.
Nested objects should use dot notation (parent.child).
Arrays should use index notation (array[0]).
Leaf nodes (actual values) should be printed as key_path: value.

Example:

user.id: 101
user.name: Alice Johnson
user.address.city: Metropolis
user.address.zipcode: 12345
devices[0].type: laptop
devices[0].brand: Dell
devices[1].type: phone
devices[1].brand: Applede
vices[0].type: laptop
devices[0].brand: Dell
devices[1].type: phone
devices[1].brand: Apple
'''

d1={
  "user": {
    "id": 101,
    "name": "Alice Johnson",
    "address": {
      "city": "Metropolis",
      "zipcode": "12345"
    }
  },
  "devices": [
    {"type": "laptop", "brand": "Dell"},
    {"type": "phone", "brand": "Apple"}
  ]
}

def expand_list(l1):
  print(f"expanding list = {l1}")
  print("----------------")
  for e in l1:
    if type(e) == list:
      return expand_list(e)
    elif type(e) == dict:
      return expand_dict(e)
    elif type(e) == str or type(e) == int or type(e) == float:
      return str(e)

def expand_dict(d2):
  print(f"expanding dict = {d2}")
  print("------------------")
  for k2,v2 in d2.items():
    if type(v2) == dict:
      return expand_dict(v2)
    elif type(v2) == list:
      return expand_list(v2)
    elif type(v2) == str or type(v2) == int or type(v2) == float:
      return str(k2) + "." + str(v2)

for k1,v1 in d1.items():
  print("---------------")
  print(f"expanding k1 = {k1} , {type(v1)}")
  print("---------------")
  r=""
  if type(v1) == dict:
    r1=expand_dict(v1)
    r2=k1 +"."+ r1
    print(r2)
  elif type(v1) == list:
    for i in range(len(v1)):
      if type(v1[i]) == dict:
        r1=expand_dict(v1[i])
      elif type(v1[i]) == list:
        r1=expand_list(v1[i])
      print(k1 +"[" + str(i) + "]" + "."+ r1)
  print("======complete=====")

