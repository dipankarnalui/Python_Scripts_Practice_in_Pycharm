menu = {
         "dosa" : 60,
         "idly" : 20,
         "upma" : 30,
         "vada" : 20,
         "poori": 50
       }

res=[]
for k,v in menu.items():
    print(k,v)
    if int(v)<= 20 and int(v)<=40:
        res.append(k)    
print(res)  # ["idly", "upma", "vada"]
