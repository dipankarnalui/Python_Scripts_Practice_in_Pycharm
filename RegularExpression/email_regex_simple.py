import re 

text1="This is a line without email \
this is my email dnalui@disco.com \
i have another id dipankarnalui@gmail.com \
"

pattern1=r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]"

out=re.findall(pattern1,text1)
print(out)
