'''
a={
   "alpha" : [10,20,25],
   "beta"  : [30,40,45,48],
   "delta" : [50,60],
   "omega" : [70,80]
  }

indentify          - dict with list as value
print [30,40]      - a["beta"][:2]
print 10           - a["alpha"][0]
last elem of beta  - a["beta"][-1]
first elem of delta- a["delta"][0] 
add 28 after 25    - a["alpha"].append(28)
delete 30          - a["beta"].pop(0)
replace 10 with 11 - a["alpha"][0] = 11 

first elem all     -  for key,value in a.items():
                          print(key, value[0]) 
add new key-value 
theta - [80,90]    - a["theta"] = [80,90]

for all total      - for key in a :
                         print(key, sum(a[key]))
'''
