'''
def split_fun(name):
    return name.split()
fname,lname=split_fun("Dipankar Nalui")
print(fname,lname)
'''

split_fun = lambda name: name.split()
fname,lname=split_fun("Dipankar Nalui")
print(fname,lname)
