f = open("input.txt",'r')
for line in f:
    if "." in line:
        print("Line Might be IP => ", line)
        words= line.split('.')
        if len(words) == 4:
            print("Line has 4 parts")
            for word in words:
                if word.isnumeric():
                    if word >=0 and  word <= 255:
                        print("valid word =>", word)
                else:
                    print("invalid")
    else:
        print("Line is not IP => ", line)

