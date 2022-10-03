from typing import Iterable


def binary_search(array: Iterable, number: int) -> int:
    """An algoritm returns the index of the number."""
    min_index = 0
    max_index = len(array) - 1

    while min_index <= max_index:
        middle_index = (min_index + max_index) // 2
        temp_number = array[middle_index]

        if temp_number == number:
            return middle_index
        elif temp_number < number:
            min_index = middle_index + 1
        elif temp_number > number:
            max_index = middle_index - 1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = int(input("Set a num for search: "))

print(f"{number} index:", binary_search(array, number))
