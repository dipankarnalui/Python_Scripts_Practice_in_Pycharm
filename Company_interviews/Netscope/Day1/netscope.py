#rank array
def changeArr(input1):
    usa=input1.copy()
    print("unsorted arr = ",usa)
    input1.sort()
    print("sorted arr = ",input1)
    ln=len(usa)
    indArr = []
    for i in range(0,ln):
        #print("ele = ",usa[i])
        #print("index = ", input1.index(usa[i]) + 1)
        indArr.append(input1.index(usa[i]) + 1)
    return indArr
if __name__ == "__main__":
    arr = [10, 8, 15, 12, 6, 20, 1]
    rank_arr=changeArr(arr)
    print("rank_array= ",rank_arr)


