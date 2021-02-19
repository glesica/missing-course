#!/usr/bin/env python3 -u

from datetime import datetime
import sys
import time

job_name = sys.argv[1]

for i in range(100):
    print(f"{job_name} [{i}] {datetime.utcnow()}")
    time.sleep(5)

