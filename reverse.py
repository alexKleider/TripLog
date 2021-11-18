#!/usr/bin/env python3

# File: reverse.py

"""
Takes a 'waypoints' file and reverses the entries.

Usage:
    ./reverse.py source_file [destination_file]
"""

import sys

if len(sys.argv) < 2:
    print(
        "Need a command line argument (waypoint file.)")
    sys.exit()


def filtered_tuples(file_name):
    with open(file_name, 'r') as source:
        for line in source:
            line = line.strip()
            if line and not line.startswith('#'):
                words = line.split()
                milage = words[0]
                descriptor = ' '.join(words[1:])
                yield (milage, descriptor)


listing = [tup for tup in filtered_tuples(sys.argv[1])]
trip_distance = float(listing[-1][0])
reverse_listing = ["{:<8.1f}{}".format(
                    trip_distance - float(entry[0]), entry[1])
                    for entry in reversed(listing)]


if len(sys.argv) == 3:
    with open(sys.argv[2], 'w') as sink:
        for line in reverse_listing:
            sink.write(line+'\n')
else:
    for line in reverse_listing:
        print(line)
