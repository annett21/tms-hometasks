from math import cos, sin, sqrt

x = float(input("Set a value for X: "))
a = float(input("Set a value for a: "))
b = float(input("Set a value for b: "))
c = float(input("Set a value for c: "))

y = (0.5 * x**2) / (a + x)
print("a) Y:", y)

y = (a + b) / (b + ((a + c) / (b + c)))
print("b) Y:", y)

y = ((cos(x**2)) ** 2 + (sin(2 * x - 1)) ** 2) ** (1 / 3)
# y = pow(((cos(x**2)) ** 2 + (sin(2 * x - 1)) ** 2), (1 / 3))
print("c) Y:", y)

y = (5 * x) + (3 * x**2) * sqrt(1 + (sin(x)) ** 2)
print("d) Y:", y)
