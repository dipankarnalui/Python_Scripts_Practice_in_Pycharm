a={
   "grp1" : {"loc":"blr","vals":[10,20,30]},
   "grp2" : {"loc":"chn","vals":[40,50,60]},
   "grp3" : {"loc":"mum","vals":[70,80,90]}
  }

'''
Indentify            - nested dict
how to print 10      - a["grp1"]["vals"][0]
how to print blr     - a["grp1"]["loc"]
last value of grp3   - a["grp3"]["vals"][-1]
print [40,50,60]     - a["grp2"]["vals"]
'''

#convert all the locations to uppercase
           #["grp1","grp2","grp3"]
for key in a:
    a[key]["loc"] = a[key]["loc"].upper()
           
#create a new key - "total" = sum(vals)
for key in a:
    a[key]["total"] = sum(a[key]["vals"]) 
