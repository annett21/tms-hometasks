from math import sqrt

a = float(input("Sat the first number: "))
b = float(input("Sat the second number: "))

y = (
    (a**2 / 3)
    + ((a**2 + 4) / b)
    + ((sqrt(a**2 + 4)) / 4)
    + ((sqrt((a**2 + 4) ** 3)) / 4)
)

print("Y:", round(y, 3))
