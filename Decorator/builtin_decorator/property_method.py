class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return 3.14 * self.radius * self.radius

c=Circle(5)
print(c.area())

