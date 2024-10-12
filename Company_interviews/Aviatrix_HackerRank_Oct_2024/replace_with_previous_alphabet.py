#Replace the alphabet with it's previous alphabet from a string
#sample input = HackerRank
#sample output = HzbjdqRzmj
def getSmallestString(s):
    r=[]
    for c in s:
        if c.isalpha() and c.islower():
            if c=='a':
                r.append('z')
            else:
                r.append(chr(ord(c)-1))
        else:
            r.append(c)
    return ''.join(r)
if __name__ == '__main__':
    s = input("Enter a string of alphabets = ")
    result = getSmallestString(s)
    print(result)
