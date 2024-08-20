import csv

def load_protocol_mapping(file_path):
    protocol_map = {}
    with open(file_path, mode="r", encoding="ascii") as file:
        reader = csv.DictReader(file)
        for row in reader:
            decimal, keyword = row["Decimal"], row["Keyword"]
            if decimal and keyword:
                protocol_map[int(decimal)] = keyword.lower()
    return protocol_map

def load_lookup_table(file_path):
    lookup = {}
    with open(file_path, mode='r', encoding='ascii') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            lookup[(row[0], row[1].lower())] = row[2]
    return lookup