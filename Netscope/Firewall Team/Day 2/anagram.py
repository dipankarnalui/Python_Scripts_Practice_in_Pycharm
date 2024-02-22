#Anagram strings
s1='cat'
s2='act' #anagram
s3='actt' #not anagram
s4='study'
s5='dusty' #anagram
s6='car'
s7='roc'
def check_anagram(s1,s2):
    flag1=False
    flag2=False
    if len(s1) == len(s2):
        for e in s2:
            if e not in s1:
                return False
        for e in s1:
            if e not in s1:
                return False
        return True
    else:
        return False
r=check_anagram(s6,s7)
if r is True:
    print("Anagram")
else:
    print("Not Anagram")


