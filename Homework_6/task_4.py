import csv


def safe_input(key):
    value = input(f"Enter a {key}: ")
    if key == "languages":
        return list(map(str.capitalize, value.split(" ")))
    return value


def add_csv_data(file_path):
    with open(file_path, "r+") as csv_f:
        data = csv.DictReader(csv_f)
        info = {key: safe_input(key) for key in data.fieldnames}
        writer = csv.DictWriter(csv_f, fieldnames=data.fieldnames)
        writer.writerow(info)


add_csv_data("Homework_6/data.csv")
