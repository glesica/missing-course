#!/usr/bin/env python3 -u

import sys
import time

for value in range(10):
    time.sleep(1)
    sys.stdout.write(f"{value}\n")
    sys.stderr.write(f"produced {value}\n")

