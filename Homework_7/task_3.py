path = "Homework_7/numbers.txt"

with open(path, "r") as f:
    numbers_sum = 0
    for line in f:
        only_numbers_line = "".join(
            (char if char.isdigit() else " " for char in line)
        )
        numbers_sum += sum([int(num) for num in only_numbers_line.split()])

print("The sum of numbers from file:", numbers_sum)
