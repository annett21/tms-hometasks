# Дан словарь, вывести новый словарь, поменяв местами ключи
# со значениями из исходного словаря

some_dict = {"name": "Ann", "surname": "Blye", "age": 23}

new_dict = {value: key for key, value in some_dict.items()}

print(new_dict)
