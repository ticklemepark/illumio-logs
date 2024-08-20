import os
import subprocess

# Define the paths to the test files
test_cases = [
    {
        "flow_log_file": "tests/test_data/flow_logs_1.txt",
        "lookup_file": "tests/test_data/lookup_1.csv",
        "output_dir": "tests/test_output_1"
    },
    {
        "flow_log_file": "tests/test_data/flow_logs_2.txt",
        "lookup_file": "tests/test_data/lookup_2.csv",
        "output_dir": "tests/test_output_2"
    },
    # Add more test cases as needed
]

# Ensure output directories exist
for case in test_cases:
    os.makedirs(case["output_dir"], exist_ok=True)

# Run the tests
for i, case in enumerate(test_cases):
    print(f"Running test case {i+1}")
    subprocess.run([
        "python3", "flow_log_parser/main.py",
        "--flow-log-file", case["flow_log_file"],
        "--lookup-file", case["lookup_file"],
        "--output-dir", case["output_dir"]
    ])
    print(f"Test case {i+1} completed.\n")
