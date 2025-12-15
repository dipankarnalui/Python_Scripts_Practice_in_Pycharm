class Person:
    def __init__(self,name,gender,age):
        self.ename = name 
        self.egender = gender 
        self.eage = age 

    def __str__(self):
        return f"{self.ename} {self.egender} {self.eage}"
    
p1 = Person("sam","m",29)
print(p1) 

#   p1 -----------------------> (ename:"sam",egender:"m",eage:29)

