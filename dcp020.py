"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point,
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Node:
    val: int
    nxt: Optional["Node"] = None

    @property
    def length(self):
        if not self.nxt:
            return 1
        return 1 + self.nxt.length


def solution(a: Node, b: Node) -> Optional[Node]:
    m = a.length
    n = b.length

    if m > n:
        for _ in range(m - n):
            a = a.nxt
    else:
        for _ in range(n - m):
            b = b.nxt

    while a != b:
        a = a.nxt
        b = b.nxt

    return a


def check(actual: Optional[Node], expected: Node):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    c2 = Node(200, Node(300))
    c1 = Node(100, c2)
    a1 = Node(1, Node(2, Node(3, Node(4, Node(5, c1)))))
    b1 = Node(10, Node(20, c1))

    a2 = Node(1000, Node(2000, c2))
    b2 = Node(10000, Node(20000, Node(30000, c2)))

    check(solution(a1, b1), c1)
    check(solution(a2, b2), c2)
