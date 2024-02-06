class Emp:
    count = 0
    total_salary = 0
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Emp.count += 1
        Emp.total_salary += salary

    @classmethod
    def display_avg_salary(cls):
        if cls.count!=0:
           print(cls.total_salary//cls.count)
        else:
           print("There are no Emps")

    def __del__(self):
        Emp.count -= 1
        Emp.total_salary -= self.__salary

if __name__ == '__main__':
    eob1 = Emp("ravi",15000)
    eob2 = Emp("john",25000)
    Emp.display_avg_salary()   # ? 20K
    eob3 = Emp("john",23000)
    Emp.display_avg_salary()   # ? 21K
    del eob1
    del eob2
    Emp.display_avg_salary()   # ? 23k

