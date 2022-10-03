import json


def safe_input(key):
    value = input(f"Enter a {key}: ")
    if key == "height":
        return int(value)
    elif key == "weight":
        return float(value)
    elif key == "languages":
        return list(map(str.capitalize, value.split(" ")))
    return value


def add_json_data(file_path):
    with open(file_path, "r") as js_f:
        new_data = json.load(js_f)
        info = {key: safe_input(key) for key in new_data[0].keys()}
        new_data.append(info)

    with open(file_path, "w") as js_f:
        json.dump(new_data, js_f, indent=4)
    print("Done!")


add_json_data("Homework_6/data.json")
