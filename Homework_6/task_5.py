import json


def read_json(file_name):
    with open(file_name, "r") as js_f:
        data = json.load(js_f)
    return data


def find_name(file_name, searched_name):
    for person in data:
        if person["name"] == searched_name:
            return person


data = read_json("Homework_6/data.json")
searched_name = input("Enter a name(with surname) for search: ")
print(find_name(data, searched_name))
