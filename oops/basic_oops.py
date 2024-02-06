class strRev():
    def __init__(self,val):
        self.myval = val

    def get_result(self):
        return self.myval

val=20
obj=strRev(val)
result=obj.get_result()
print(result)