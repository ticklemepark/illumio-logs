import csv

def write_csv_tag(data, file_path, headers):
    with open(file_path, mode="w", newline='', encoding="ascii") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for key,value in data.items():
            writer.writerow([key,value])

def write_csv_total(data, file_path, headers):
    with open(file_path, mode="w", newline='', encoding="ascii") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for (key1, key2), value in data.items():
            writer.writerow([key1, key2, value])
