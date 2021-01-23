#!/usr/bin/env python3

# Read a file, parse each line as an integer,
# and then determine how many of them are prime
# numbers. Don't be particularly efficient.

import sys

def is_prime(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    for i in range(3, n):
        if n % i == 0:
            return False
    
    return True

count = 0
filename = sys.argv[1]
with open(filename, "r") as in_file:
    for line in in_file:
        value = int(line)
        result = is_prime(value)
        count += int(result)

print(f"{filename} {count}")

