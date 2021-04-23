#!/usr/bin/env python3

from multiprocessing import Process
from threading import Thread
from time import sleep, time


# This is a version of the Thread / Process API that runs the tasks given to it
# in serial, in other words with no concurrency at all, to illustrate the
# difference between serial and concurrent execution. Note that the order in
# which the tasks finish will be different using Serial.
class Serial:
    def __init__(self, target, args):
        self.target = target
        self.args = args

    def start(self):
        pass

    def join(self):
        self.target(*self.args)


# This is just so that we can use smaller numbers later.
BASE_N = 10000

# This is the class we will use to provide concurrency. Either Serial, Thread or
# Process.
CONCURRENCY_CLASS = Serial


# The function that will run concurrently. It does some nonsense work just to
# keep the CPU busy for a few seconds.
def work(name: str, multiplier: int):
    print(f"{name}: start")

    # Just calculate a bunch of Fibonacci numbers
    N = multiplier * BASE_N
    a = 0
    b = 1
    for n in range(N):
        c = a + b
        a = b
        b = c

    print(f"{name}: work({N}) = {str(b)[:4]}...")
    print(f"{name}: end")


def _main():
    print(f"using {CONCURRENCY_CLASS.__name__}")
    print("")

    # Create some tasks that we will execute concurrently, and perhaps in
    # parallel if we use the Process class instead of the Thread class (see
    # below for an explanation).
    tasks = [
        ("foo", 25),
        ("bar", 75),
        ("baz", 50),
    ]

    # Create one logical thread of execution for each of our tasks. This might
    # mean a Thread, or it might mean a Process. If we use a Thread, then when
    # the code runs on the standard Python interpreter (CPython), the tasks will
    # not run in parallel, but they will nonetheless run concurrently. If we use
    # a Process, then a new Python interpreter will be spawned for each task and
    # they will run in parallel.
    threads = [CONCURRENCY_CLASS(target=work, args=a) for a in tasks]

    # We need to start each logical thread of execution running. Before we do
    # this, we note the time so that we can track how long it takes.
    ts = time()
    for t in threads:
        t.start()

    # When we wait for a concurrent task to finish we generally say that we
    # "join" the task (thread or process). This is a funny term, but it makes
    # sense in the context of the C programming language. Once all logical
    # threads have completed, we note the time.
    for t in threads:
        t.join()
    te = time()

    # Print how long the tasks took to complete. This will differ based on
    # whether we used Thread or Process. In general, Process will be faster,
    # although the increase in performance will be sub-linear because of the
    # overhead required to start up several new instances of the Python
    # interpreter.
    print("")
    print(f"total time: {te - ts:.3f}s")


if __name__ == "__main__":
    _main()

