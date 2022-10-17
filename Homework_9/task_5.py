from math import atan, degrees


class RightTriangle:
    def __init__(self, cathet_a, cathet_b):
        self.cathet_a = cathet_a
        self.cathet_b = cathet_b

    def increase_cathet_a(self, percent):
        self.cathet_a += self.cathet_a * percent / 100

    def increase_cathet_b(self, percent):
        self.cathet_b += self.cathet_b * percent / 100

    def decrease_cathet_a(self, percent):
        self.cathet_a -= self.cathet_a * percent / 100

    def decrease_cathet_b(self, percent):
        self.cathet_b -= self.cathet_b * percent / 100

    @property
    def circumcircle_radius(self):
        return ((self.cathet_a**2 + self.cathet_b**2) ** (0.5)) / 2

    @property
    def perimeter(self):
        return (
            self.cathet_a
            + self.cathet_b
            + ((self.cathet_a**2 + self.cathet_b**2) ** (0.5))
        )

    @property
    def alfa_angel(self):
        return round(degrees(atan(self.cathet_a / self.cathet_b)), 2)

    @property
    def beta_angel(self):
        return round(degrees(atan(self.cathet_b / self.cathet_a)), 2)


triangle = RightTriangle(5, 8.66)
print(triangle.circumcircle_radius)
print(triangle.perimeter)
print(triangle.beta_angel)
triangle.increase_cathet_a(2)
print(triangle.cathet_a)

triangle = RightTriangle(3, 4)
print(triangle.perimeter)
