import collections
# input data
alst = ["blr","chn","mum","hyd","tpuram","blr","chn","blr"]
# function factory which return a default value
def default():
  return 0
# define a empty dict
freq = collections.defaultdict(default,{})
# finds the frequency of each element
for city in alst:
   freq[city] = freq[city] + 1
print(freq)
dup = []
for key,value in freq.items():
    if value>1:
        dup.append(key)
print("DUPLICATEs = ",dup)