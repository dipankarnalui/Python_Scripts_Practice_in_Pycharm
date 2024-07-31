import re

data = "12-13 14,15:16"
#res = re.split(r"[\-\s,:]", data)
res = re.split(r"\W", data)

print(res)
