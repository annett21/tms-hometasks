def greatest_divisor(num_1, num_2):
    if num_2 == 0:
        return num_1
    return greatest_divisor(num_2, num_1 % num_2)


num_1 = int(input("Set a number: "))
num_2 = int(input("Set a number: "))
print(
    f"Greatest common divisor for {num_1} and {num_2}:",
    greatest_divisor(num_1, num_2),
)
