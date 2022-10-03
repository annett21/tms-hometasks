from math import cos, sin

x = float(input("Set a value for X: "))

y = cos(x) + sin(x)
print("Y:", round(y, 5))

tangent = sin(x) / cos(x)
print("Tg:", round(tangent, 5))

cotangent = 1 / tangent
print("Ctg:", round(cotangent, 5))
