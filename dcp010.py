"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import time


def schedule(f, n: int):
    sec = n / 1000
    start = time.time()

    def __sched():
        while True:
            if time.time() >= start + sec:
                f()
                return
            yield

    co = __sched()
    while True:
        try:
            next(co)
        except Exception:
            return


if __name__ == "__main__":
    schedule(lambda: print("Hello!"), 1000)
