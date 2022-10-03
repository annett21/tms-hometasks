import json


def read_json(file_name):
    with open(file_name, "r") as js_f:
        data = json.load(js_f)
    return data


def filter_language(data, language):
    language_users = []
    for person in data:
        if language in person["languages"]:
            language_users.append(person["name"])
    return language_users


data = read_json("Homework_6/data.json")
checked_language = input("Enter language for search: ").capitalize()
print(
    f"Could use {checked_language}:",
    filter_language(data, checked_language),
)
