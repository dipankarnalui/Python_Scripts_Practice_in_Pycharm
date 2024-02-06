# Python3 code to demonstrate
# Separating odd and even index elements
# Using list slicing

test_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("The original list : " + str(test_list))

# Using list slicing
print(test_list[0:6])
print(test_list[0::6])

#To print odd index
print(test_list[1::2])
#To print even index
print(test_list[0::2])
#starting from 10th index to end
print(test_list[10::])
#starting from 10th index to end by giving 2 gap
print(test_list[10::2])
print(test_list[10:])

res = test_list[::2] + test_list[1::2]
print("Separated odd and even index list : " + str(res))