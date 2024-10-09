'''
Implement a restaurant waitlist data structure. It should support the following features:
1) A party of customers can join the waitlist.
2) A previously joined party can leave the waitlist at any time.
3) The restaurant can ask the data structure for the first party that fits a given table size (a table size is given as an argument).
'''

table = 5

d1 = []

'''
d1={1:[c6],
        2:["c1","c4"],
        3:[c2],
        4:[c3],
        5:[c5,c10]                  
        }
'''


def add_waitlist(c, l):
    d1[l].append(c)


def remove_waitlist(c, l):
    for k, v in d1.items():
        if k == l:
            for i in range(len(d1[k] - 1)):
                if d1[k][i] == c:
                    del d1[k][i]


def allocate_table(ts):
    keys = d1.keys()
    for i in range(len(keys) - 1, -1, -1):
        if keys[i] == ts and len(keys[i]) > 0:
            return keys[i][0]
            remove
            d1[keys[i]][0]
            break
        elif keys[i] == ts and len(keys[i])==0:
            ts = ts - 1


if __name__ == "main":
    ts=5
    cus, l = input("Enter cust name, count separated by comma").split(",")
    add_waitlist(cus, l)
    remove_waitlist(cus, l)
    allocate_table(ts)
