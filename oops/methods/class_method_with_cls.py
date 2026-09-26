class A():
    name="Dipankar" #class variable
    @classmethod
    def method1(cls):
        print(cls.name)

a=A()
a.method1()
