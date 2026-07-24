def greet(msg,*names):

    print(names)
    print(type(names))

    for name in names:
        print(msg,name)

greet("Hello","Dipankar","Nalui")

