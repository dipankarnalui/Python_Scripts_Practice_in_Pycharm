grps = {
         "alpha" : 1, 
         "beta"  : 2, 
         "delta" : 3, 
         "omega" : 4
       }

#method-1:-
#-----------
# treat dict like a list - fetch only the keys

           #["alpha","beta","delta","omega"]
for key in grps: 
    print(key,grps[key])

#method-2:-
#-----------
          #   key   val
          #[("alpha",1),("beta",2),("delta",3),("omega",4)]
for key,value in grps.items():  
    print(key,value)

