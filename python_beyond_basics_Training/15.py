import subprocess
folder = r"c:\pyprogs\sample"
output = subprocess.check_output("dir "+folder,shell=True)
output = output.decode("utf-8")
#print(output)
# from the "dir" we need skip the first 5 lines
#                we need skip the last 3 lines
# remove first 5 lines & last 3 lines
outlst = output.split("\n")[5:-3]
#print("\n".join(outlst))
result = {}   # defined a empty dict
for elem in outlst:
   if "<DIR>" in elem:
      continue
   datestr, timestr, size, filename = elem.split()
   #print(datestr,timestr,size,filename)
          #key         #value
   result[filename] = int(size.replace(",",""))
   print(result)
print(sum(result.values()))