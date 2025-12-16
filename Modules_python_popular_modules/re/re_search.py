import re

str1="Hello World"
pattern="World"
r=re.search(pattern,str1)
print(r)
print("Found the pattern = ",r.group())
print("Found at start index = ",r.start())
print("Found at end index = ",r.end())


