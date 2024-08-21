def parse_flow_logs(file_path, protocol_map):
    logs = []
    with open(file_path, "r", encoding="ascii") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    for line in lines:
        line = line.split(" ")
        if len(line) != 14:
            continue
        dstport, protocol = line[6], protocol_map[int(line[7])].lower()
        logs.append((dstport, protocol))

    return logs

def process_logs(logs, lookup):
    tag_count = {}
    port_protocol_count = {}

    for log in logs:
        if log in lookup:
            if lookup[log] not in tag_count:
                tag_count[lookup[log]] = 1
            else:
                tag_count[lookup[log]] += 1
            if log not in port_protocol_count:
                port_protocol_count[log] = 1
            else:
                port_protocol_count[log] += 1
        else:
            if "Untagged" not in tag_count:
                tag_count["Untagged"] = 1
            else:
                tag_count["Untagged"] += 1

    return tag_count, port_protocol_count