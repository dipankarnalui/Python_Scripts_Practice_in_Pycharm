import collections

filename = "C:\\pyprogs\\poem.txt"
try:
    f1 = open(filename, "r")
    # converted complete file into lower case - case insensitive
    strbuffer = f1.read().lower()
    # deleting the special chars - exclude special chars
    strbuffer = strbuffer.replace(",", "")
    strbuffer = strbuffer.replace("[", "")
    strbuffer = strbuffer.replace("]", "")
    strbuffer = strbuffer.replace('"', '')
    strbuffer = strbuffer.replace('.', '')
    # scalar into a vector
    words = strbuffer.split()
    print(words)

    # frequency count
    freq = collections.Counter(words)
    print(freq)
    print(freq.most_common(1))
except FileNotFoundError as e:
    print("File not found")
else:
    f1.close()