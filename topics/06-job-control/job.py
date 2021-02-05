#!/usr/bin/env python3 -u

from datetime import datetime
import sys
import time

job_name = sys.argv[1]

while True:
    print(f"{job_name} {datetime.utcnow()}")
    time.sleep(5)

