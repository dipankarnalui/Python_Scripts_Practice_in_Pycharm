'''
n      next line
s      step into a function
c      continue until next breakpoint
l      list source code around current line
p x    print variable x
pp x   pretty-print variable x
w      show call stack
u      move up stack frame
d      move down stack frame
q      quit debugger
h      help
'''

def divide(a, b):
    result = a / b
    return result

x = 10
y = 0
breakpoint()
print(divide(x, y))
