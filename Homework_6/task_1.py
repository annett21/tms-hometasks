import json


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


with open("Homework_6/data.json", "r") as json_file:
    json_string = json_file.read()
    csv_string = json_to_csv(json_string)
    print(json_string)
    print(csv_string)
