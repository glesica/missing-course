#!/usr/bin/env python3 -u

import sys

for value in sys.stdin:
    sys.stderr.write(f"consumed {value}\n")

