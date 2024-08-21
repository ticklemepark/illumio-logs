# illumio-logs

This repository contains a Python script designed to parse flow log data and map each row to a corresponding tag based on a lookup table. The lookup table is provided as a CSV file with columns for destination port (`dstport`), protocol, and tag. The script generates an output file summarizing the count of matches for each tag and the count of matches for each port/protocol combination.

## How It Works

1. **Input Files**: 
   - A plain text ASCII file containing flow log data. Each log entry is expected to be line-separated.
   - A CSV file containing the lookup table with three columns: `dstport`, `protocol`, and `tag`.

2. **Processing**:
   - The script reads the flow log file and extracts relevant information such as the destination port and protocol from each log entry.
   - It matches the extracted data against the lookup table to determine the appropriate tag for each log entry.
   - The script counts the occurrences of each tag and each port/protocol combination.

3. **Output**:
   - A CSV file listing each tag and its corresponding count.
   - A CSV file listing each port/protocol combination that appears in the lookup and its corresponding count.

## Assumptions

- **Default Ordering of Logs**: 
  - The flow log entries are assumed to follow a default structure where the fields are ordered consistently (dstport and protocol should be the 7th and 8th field respectively).
  
- **Version 2 Logs**: 
  - The script is designed to work specifically with flow log data in version 2 format. The format and field positions may differ in other versions.

- **Fixed Number of Fields**:
  - Each flow log entry is expected to contain exactly 14 fields. Entries with more or fewer fields may not be processed correctly.

- **Protocol Identification**:
  - The script only identifies and maps official protocols as per the IANA protocol numbers. Any non-standard or rogue protocols will not be identified or tagged.

## Running the Script

1. Make sure you're in the parent directory and run python3 tests/run_tests.py
2. If you want to add more tests, put the input files into the tests/test_data folder then add the path to the run_tests.py file so it runs all the test cases. Two are already given.


## Test Cases

I used the default lookup.csv and flow_logs.txt input files but also created my own test case. Primarily the main edge cases were logs with missing fields, maximum and minimum port numbers, nonexistent protocol, repeated port and protocol pairs, incorrect protocol mapping (in case the protocol mapping in logs is incorrect or missing, the program should label it as "untagged")
