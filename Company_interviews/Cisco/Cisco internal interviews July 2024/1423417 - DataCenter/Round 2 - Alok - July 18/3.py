#code is given
#Do white box testing
#Find the issues in the code
#Suggest code improvement
#needed for Code review by seniors
#Data Type checking, division by zero, boundary value analysis etc.


def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# Test the function
numbers = [10, 20, 30, 40, 50]
print("Average:", calculate_average(numbers))

