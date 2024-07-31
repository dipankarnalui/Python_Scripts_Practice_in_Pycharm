def convert(data):
    eight=8
    four=4
    zero=0
    three=3
    new_str=""
    for e in data.split(","):
        if e == "eight":
            new_str.join(str(eight))
        elif e == "four":
                new_str.join(str(four))
        elif e == "zero":
            new_str.join(str(zero))
        elif e == "three":
            new_str.join(str(three))
    return new_str
data="eight,four,zero,three"
res = convert(data)
print(res) # 8403
