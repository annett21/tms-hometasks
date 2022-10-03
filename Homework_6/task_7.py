# Функция фильтра по росту - среди всех сотрудников, у которых год рождения
# меньше заданного посчитать средний рост

import json


def read_json(file_name):
    with open(file_name, "r") as js_f:
        data = json.load(js_f)
    return data


def filter_height(data, birthday):
    users_height = []
    for person in data:
        if person["birthday"].split(".")[-1] < birthday:
            users_height.append(person["height"])
    return sum(users_height) / len(users_height)


data = read_json("Homework_6/data.json")
checked_birtday = input("Enter a year of birth: ")
print("Average height:", filter_height(data, checked_birtday))
