class multi():
    def __init__(self, inp):
        self.inp=inp
        self.store = []
        self.cnt = len(inp)
        self.input2 = []
        self.final_list = []

    def mul(self):
        # print(input2)
        result = 1
        for ele in self.input2:
            result = result * ele
        return result

    def get_result(self):
        for i in range(0, self.cnt):
            self.input2 = self.inp.copy()
            print("current element = ", input[i])
            self.input2.pop(i)
            # print("After deleting input2 = ", input2)
            # print("After deleting input = ", input)
            mul_result = self.mul()
            # print(mul_result)
            self.final_list.append(mul_result)
        return self.final_list

input = [1, 2, 3, 4, 5]
obj = multi(input)
final_list=obj.get_result()
print("Output = ", final_list)