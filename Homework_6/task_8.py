import json
import csv


def read_json(file_name):
    with open(file_name, "r") as js_f:
        data = json.load(js_f)
    return data


def json_to_csv(json_string):
    json_data = json.loads(json_string)

    csv_headers = [key for key in json_data[0]]
    csv_rows = [csv_headers, ]

    for item in json_data:
        csv_row = []
        for header in csv_headers:
            csv_row.append(str(item[header]))
        csv_rows.append(csv_row)

    return "\n".join((",".join(csv_raw) for csv_raw in csv_rows))


def write_json_to_csv(data, path):
    with open(path.split(".")[0] + ".csv", "w") as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        print("Done!")


def find_name(data):
    searched_name = input("Enter a name (with surname) for search: ")
    for person in data:
        if person["name"] == searched_name:
            return person


def safe_input(key):
    value = input(f"Enter a {key}: ")
    if key == "height":
        return int(value)
    elif key == "weight":
        return float(value)
    elif key == "languages":
        return list(map(str.capitalize, value.split(" ")))
    return value


def add_json_data(data, path):
    info = {key: safe_input(key) for key in data[0].keys()}
    data.append(info)

    with open(path, "w") as js_f:
        json.dump(data, js_f, indent=4)
    print("Done!")


def filter_language(data, language):
    language_users = []
    for person in data:
        if language in person["languages"]:
            language_users.append(person["name"])
    return language_users


def filter_height(data):
    birthday = input("Enter a year of birth: ")
    users_height = []
    for person in data:
        if person["birthday"].split(".")[-1] < birthday:
            users_height.append(person["height"])
    return sum(users_height) / len(users_height)


path = "Homework_6/data.json"
answer = 0
while answer != 7:
    data = read_json(path)
    answer = int(
        input(
            "Choose actions:\n"
            "1. Make csv from json\n"
            "2. Save data to csv file\n"
            "3. Add person\n"
            "4. Find info by name\n"
            "5. Find person by language\n"
            "6. Find average height by date of birth\n"
            "7. Exit\n"
            ">>> "
        )
    )
    if answer == 1:
        with open(path, "r") as json_file:
            json_string = json_file.read()
            csv_string = json_to_csv(json_string)
            print(csv_string)
    elif answer == 2:
        write_json_to_csv(data, path)
    elif answer == 3:
        add_json_data(data, path)
    elif answer == 4:
        print(find_name(data))
    elif answer == 5:
        checked_language = input("Enter language for search: ").capitalize()
        print(
            f"Could use {checked_language}:",
            filter_language(data, checked_language),
        )
    elif answer == 6:
        print("Average height:", filter_height(data))
