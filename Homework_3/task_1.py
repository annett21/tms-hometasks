# Написать filter  с лямбда-функцией определяющей число чётное/нечётное.

some_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(filter(lambda x: x % 2 == 0, some_list)))
