#!/usr/bin/python3

import sys

# Define the status codes to track
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize the metrics
total_size = 0
status_counts = {code: 0 for code in status_codes}

try:
    # Read the input line by line
    for i, line in enumerate(sys.stdin, 1):
        # Parse the line
        parts = line.split()
        if len(parts) != 7:
            raise ValueError(f"Invalid input format on line {i}")
        ip, date, method, path, protocol, status, size = parts
        
        # Update the metrics
        total_size += int(size)
        if int(status) in status_codes:
            status_counts[int(status)] += 1
        
        # Print the metrics every 10 lines
        if i % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print(f"{code}: {status_counts[code]}")
            print()
            
except KeyboardInterrupt:
    # Handle keyboard interrupt
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")
