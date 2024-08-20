import argparse

from mapping import *
from output import *
from parsing import *

def main(flow_log_file, lookup_file, output_dir):
    # Load protocol mapping
    protocol_map = load_protocol_mapping('tests/test_data/protocol-numbers-1.csv')

    # Parse flow logs
    logs = parse_flow_logs(flow_log_file, protocol_map)

    # Load lookup table
    lookup = load_lookup_table(lookup_file)

    # Process logs and generate output data
    tag_count, port_protocol_count = process_logs(logs, lookup)

    # Write output to CSV files
    write_csv_tag(tag_count, f"{output_dir}/tag_counts.csv", ["Tag", "Count"])
    write_csv_total(port_protocol_count, f"{output_dir}/port_protocol_counts.csv", ["Port", "Protocol", "Count"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flow Log Parser")
    parser.add_argument("--flow-log-file", required=True, help="Path to the flow log file")
    parser.add_argument("--lookup-file", required=True, help="Path to the lookup CSV file")
    parser.add_argument("--output-dir", required=True, help="Directory to save the output CSV files")
    
    args = parser.parse_args()
    main(args.flow_log_file, args.lookup_file, args.output_dir)
