#Tupple unpacking
#a,b,c=10,20,30,40,50,60,70
#*a,b,c=10,20,30,40,50,60,70
#a,*b,c=10,20,30,40,50,60,70
#a,b,*c=10,20,30,40,50,60,70
#*a,b,c=10,20
#a,*b,c=10,20
#a,b,*c=10,20
#a,*b,*c=10,20 #error, not allowed multiple * in one statement
*a,b,c=10 #can not unpack
print(a)
print(b)
print(c)