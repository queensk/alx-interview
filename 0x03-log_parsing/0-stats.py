#!/usr/bin/python3
"""
Read stdin
"""
import sys

def print_stats(total_size, status_codes):
    """
    print stats code
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        count = status_codes[code]
        print("{}: {}".format(code, count))

def process_logs():
    """
    print logs
    """
    total_size = 0
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            if line_count > 10:
                print_stats(total_size, status_codes)
                line_count = 1

            parts = line.split()
            if len(parts) != 9:
                continue
            try:
                size = int(parts[-1])
            except ValueError:
                continue

            total_size += size
            status_codes[parts[-2]] = status_codes.get(parts[-2], 0) + 1

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)

process_logs()
