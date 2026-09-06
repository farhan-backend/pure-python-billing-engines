class Circle:
    def __init__(self, radius, unit):
        self.radius = radius
        self.unit = unit

    def area(self):
        return (22 / 7) * (self.radius ** 2)

    def perimeter(self):
        return 2 * (22 / 7) * self.radius

    def summary(self):
        p = self.perimeter()
        a = self.area()
        return (
            f"If the radius of the circle is {self.radius:.2f} {self.unit},\n"
            f"then the Perimeter of the circle will be {p:.2f} {self.unit},\n"
            f"and its Area will be {a:.2f} {self.unit}^2.\n"
        )



c1 = Circle(14/3, "cm")
print(c1.summary())

c2 = Circle(63, "m")
print(c2.summary())

 
