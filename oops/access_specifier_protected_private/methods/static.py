class Demo:
    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass

'''
Instance method: Uses self; works with object data.
Class method: Uses cls; works with class-level data.
Static method: Doesn't receive self or cls; behaves like a regular function inside the class.
'''