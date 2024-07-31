l1=["10","20","30","40"]
marks= [int(e) for e in l1 ] #Conversion "str of list" to "int of list"
print(marks)

#alternative
s1="10","20","30","40"
print(type(s1)) #s1 is tuple
#l2=s1.split(",") #split is not for tuple
m2=(list(map(int,s1)))
print(m2)