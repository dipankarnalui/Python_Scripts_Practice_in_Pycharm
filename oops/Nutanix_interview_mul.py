input = [1, 2, 3, 4, 5]
store = []
cnt=len(input)
print("Total element ",cnt )
input2=[]
final_list=[]

def mul(input2):
    #print(input2)
    result=1
    for ele in input2:
        result=result * ele
    return result


for i in range(0,cnt):
    input2 = input.copy()
    #print("current element = ", input[i])
    input2.pop(i)
    #print("After deleting input2 = ", input2)
    #print("After deleting input = ", input)
    mul_result = mul(input2)
    #print(mul_result)
    final_list.append(mul_result)

print("Output = ", final_list)
