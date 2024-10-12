import re 

text1=" This is a sample \
this is ipv4 123.12.34.12 \
this is another 10.10.30.56 \
this is not \
"

pattern=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

out=re.findall(pattern,text1)
print(out)

