class StatusProcessor():
    def __init__(self):
        pass
    def public_method(self):
        print("public called")
    def _private_method(self):
        print("private called")

obj=StatusProcessor()
obj.public_method()
obj._private_method()