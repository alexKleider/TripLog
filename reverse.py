#!/usr/bin/env python3

# File: reverse.py

"""
Takes a 'waypoints' file and reverses the entries.
e.g. Compare files 'nov2021waypoints' and 'nov_reversed'
Preserves leading commented lines appending them to end of output.
All commented lines after the first data line are ignored.
If a destination file is not specified user is prompted for one;
if none is provided, output goes to stdout.

Usage:
    ./reverse.py source_file [destination_file]
"""

import sys

args = sys.argv[1:]
nargs = len(args)


def filtered_tuples(file_name):
    dealing_with_headers = True
    with open(file_name, 'r') as source:
        for line in source:
            line = line.strip()
            if line.startswith('#') and dealing_with_headers:
                yield ("-1", line)
            elif line and not line.startswith('#'):
                dealing_with_headers = False
                words = line.split()
                milage = words[0]
                descriptor = ' '.join(words[1:])
                yield (milage, descriptor)


if nargs < 1:
    print(
        "Need a command line argument (waypoint file.)")
    sys.exit()

if nargs > 1:
    dest = args[1]
else:
    print("Enter nothing to have output printed to the terminal or..")
    dest = input("Provide a destination file name: ")

listing = [tup for tup in filtered_tuples(args[0])]
trip_distance = float(listing[-1][0])
reverse_listing = ["{:<8.1f}{}".format(
                    trip_distance - float(entry[0]), entry[1])
                    if not (float(entry[0]) < 0)
                    else entry[1]
                    for entry in reversed(listing)]

if dest:
    sink = open(dest, 'w')
    need2close = True
else:
    sink = sys.stdout
    need2close = False

for line in reverse_listing:
    print(line, file=sink)
if need2close:
    sink.close()
