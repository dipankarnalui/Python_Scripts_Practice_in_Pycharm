fname=input("Enter first name : ")
mname=input("Enter mid name : ")
lname=input("Enter last name : ")

print(fname.upper(),mname.upper(),lname.upper())
print(f"{fname}-{mname}-{lname}")
print(f"{fname},{mname},{lname}")

##second method====>

r1="%s %s %s" %(fname.upper(),mname.upper(),lname.upper())
r2="%s-%s-%s" %(fname,mname,lname)
r3="%s,%s,%s" %(fname,mname,lname)

print(r1)
print(r2)
print(r3)