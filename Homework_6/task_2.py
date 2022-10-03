import json
import csv


def write_json_to_csv(file_name: str) -> None:
    with open(file_name, "r") as js_f, open(
        file_name.split(".")[0] + ".csv", "w"
    ) as csv_f:
        new_data = json.load(js_f)
        writer = csv.DictWriter(csv_f, fieldnames=new_data[0].keys())
        writer.writeheader()
        writer.writerows(new_data)
        print("Done!")


write_json_to_csv("Homework_6/data.json")
