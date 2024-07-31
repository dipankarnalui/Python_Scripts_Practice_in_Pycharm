def convert(data):
    encode={"zero":"0","one":"1","two":"2","three":"3",
    "four":"4","five":"5","six":"6","seven":"7",
    "eight":"8","nine":"9"}
    alst = []
    for digit in data.split(","):
        alst.append(encode[digit])

        return int("".join(alst))


data="eight,four,zero,three"
res = convert(data)
print(res) # 8403

