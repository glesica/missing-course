#!/usr/bin/env python3

# Print a list of large, random-ish numbers.

import random
import sys

count = int(sys.argv[1])
size = int(sys.argv[2])
for _ in range(count):
    number = random.randint(2**size, 2**(size + 1))
    print(number)

