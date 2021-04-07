#!/usr/bin/env python3

# Usage:
# ./table_lookup.py <TABLE> <HASH>
# Look up the give HASH value in the rainbow table stored in the file TABLE. If
# a password is found, print it.

from sys import argv

table_filename = argv[1]
hashed_password = argv[2]

found_password = ""

# Note that we're doing a naive, linear lookup here. If we had a larger rainbow
# table, we would use a smarter data structure to get sub-linear lookups.

with open(table_filename, "r") as table_file:
    for line in table_file:
        line_hash, line_password = line.split(" ")
        if line_hash == hashed_password:
            found_password = line_password
            break

if found_password:
    print(f"password: {found_password}")
else:
    print("hash not found")

