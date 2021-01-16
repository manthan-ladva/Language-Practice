class circle():
    pie = 3.14
    def __init__(self, radius):
        self.radius = radius
        a = 2 * self.pie * self.radius
        print(a)
    def area(self):
        a = self.pie * self.radius * self.radius
        print(a)

c = circle(10)
c.area()
