def grep(filename="one.txt",word="sample"):
    with open(filename) as f1:
         for line in f1:
             if word in line:
                print(line)

grep()

'''
1) function name    - grep
2) how many args    - 2
3) datatype of args - string, string
4) type of function - default
5) does it return ? - no
6) is it a pure fn? - no
7) local vars       - filename,word,line,f1
8) how to call      - grep()
                      grep("emp.txt")
                      grep("emp.txt","sales")
                      
'''