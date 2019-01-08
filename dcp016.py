from typing import List
from queue import Queue
"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""


class API:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.buf: List[str] = []

    def record(self, order_id: str):
        self.buf.insert(0, order_id)
        if len(self.buf) >= self.capacity:
            self.buf = self.buf[:self.capacity]

    def get_last(self, i: int):
        return self.buf[i]


def check(actual: str, expected: str):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    api = API(6)
    api.record("A")
    api.record("B")
    api.record("C")
    api.record("D")
    api.record("E")
    api.record("F")

    check(api.get_last(0), "F")
    check(api.get_last(1), "E")
    check(api.get_last(2), "D")
    check(api.get_last(3), "C")
    check(api.get_last(4), "B")
    check(api.get_last(5), "A")

    api.record("G")
    api.record("H")
    api.record("I")

    check(api.get_last(0), "I")
    check(api.get_last(1), "H")
    check(api.get_last(2), "G")
