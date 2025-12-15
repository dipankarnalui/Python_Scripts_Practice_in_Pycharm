def insert_zero(alst,num=0):
  newlst = []
  for elem in alst:
      newlst.append(elem)
      newlst.append(num)
  return newlst


alst = [10,15,20,18,16]
res = insert_zero(alst,0)
print(res)  #[10,0,15,0,20,0,18,0,16,0] 

