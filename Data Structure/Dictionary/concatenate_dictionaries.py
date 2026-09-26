#dictionary concatenation
#if both dictionaries have the same key, the value from d2 will overwrite the value from d1.

d1={
    "k1":"v1",
    "k2":"v2"
}
print(d1)
d2={
    "k2":"v3",
    "k4":"v4"
}
print(d2)

#d3=d1+d2 #not supported
#print(d3)


d4=d1 | d2 #supported
print(d4)

d5={**d1,**d2}
print(d5)

