def get_key(atab,limit=10):
   alst = []
   for key,value in atab.items():
       if value>=limit:
          alst.append(key)

   return alst
'''

1) function name    - get_key
2) how many args    - 2
3) datatype of args - dict, int
4) type of function - hybrid
5) does it return ? - yes
6) is it a pure fn? - yes
7) local vars       - atab,limit,alst,key,value
8) how to call      - result=get_key({"a":20,"b":5})
                      print(result)
                      result=get_key({"a":2,"b":7,"c":8}, 5)
                      print(result)

'''