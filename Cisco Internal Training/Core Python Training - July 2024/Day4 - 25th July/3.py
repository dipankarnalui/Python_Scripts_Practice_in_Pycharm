data = "eight,four,zero,three"
numbersmap = {
    "eight": '8',
    "four": '4',
    "zero": '0',
    "three": '3',
}


def convert(text):
    numbersconverted = list(map(lambda x: numbersmap[x], text.split(",")))
    return int("".join(numbersconverted))


print(convert(data))
