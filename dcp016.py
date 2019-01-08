from typing import List
from queue import Queue
"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following Log:
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""


class Log:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.buf: List[str] = [""] * self.capacity
        self.head = 0

    def record(self, order_id: str):
        self.buf[self.head] = order_id
        self.head = (self.head + 1) % self.capacity

    def get_last(self, i: int):
        index = self.head - 1 - i
        if index < 0:
            index += self.capacity
        return self.buf[index]


def check(actual: str, expected: str):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    log = Log(6)
    log.record("A")
    log.record("B")
    log.record("C")
    log.record("D")
    log.record("E")
    log.record("F")

    check(log.get_last(0), "F")
    check(log.get_last(1), "E")
    check(log.get_last(2), "D")
    check(log.get_last(3), "C")
    check(log.get_last(4), "B")
    check(log.get_last(5), "A")

    log.record("G")
    log.record("H")
    log.record("I")

    check(log.get_last(0), "I")
    check(log.get_last(1), "H")
    check(log.get_last(2), "G")
