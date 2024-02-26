if __name__ == '__main__':
    n = int(input("Enter the number of students "))
    student_marks = {}
    for _ in range(n):
        print("Enter student name and marks separated by space ")
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter student for which the average will be calculated ")
    result = 0
    for key,value in student_marks.items():
        #print(key, value)
        if key == query_name:
            #print(query_name, value)
            for e in value:
                #print(e)
                result=result + e
                #print(result)
            #print("sum = ", result)
            length=len(value)
            average = float(result) / length
            # print(float(average))
            out = round(average, 2)
            print("%.2f" % out)

'''
Enter the number of students 3
Enter student name and marks separated by space 
a 34.89 23.09 12.34
Enter student name and marks separated by space 
b 5 67.9 12.2
Enter student name and marks separated by space 
c 24.6 90.4 23.1
Enter student for which the average will be calculated c
Avg =  46.03
'''