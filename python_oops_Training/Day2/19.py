class Singleton:
    flag = True  # indicator
    _inst = None  # holds the address of your object

    def __new__(cls, *args, **kwargs):
        if cls.flag:
            cls._inst = super().__new__(cls, *args, **kwargs)
            cls.flag = False
        return cls._inst

    def fun(self):
        print("Fun...")


s1 = Singleton()
s2 = Singleton()
print(id(s1))
print(id(s2))

s1.fun()
s2.fun()
