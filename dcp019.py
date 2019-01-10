from typing import List
"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost
to build the nth house with kth color, return the minimum cost which achieves this goal.

[
    [1]
]

> 1

[
    [1, 2],
    [1, 2],
]

> 1 + 2 = 3

[
    [1, 2],
    [100, 150],
    [300, 20],
]

> max(1 + 150 + 300, 2 + 100 + 20) = 122
"""


class Node:
    def __init__(self, n: int, k: int, cost: int, matrix: List[List[int]]):
        self.n: int = n
        self.k: int = k
        self.cost: int = cost
        self.matrix: List[List[int]] = matrix

        self.__num_houses = len(matrix)
        self.__num_colors = len(matrix[0])

    @property
    def children(self):
        if self.n == self.__num_houses - 1:
            return []

        # 'k != self.k' is for avoiding neighboring same color
        return [
            Node(self.n + 1, k, self.matrix[self.n + 1][k], self.matrix)
            for k in range(self.__num_colors) if k != self.k
        ]

    @property
    def min_cost(self):
        if len(self.children) == 0:
            return self.cost

        return self.cost + min([child.min_cost for child in self.children])


def solution(nk: List[List[int]]) -> int:
    root = Node(-1, -1, 0, nk)
    return root.min_cost


def check(actual: int, expected: int):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    m1 = [[1, 2]]
    ans1 = 1

    m2 = [
        [1, 2],
        [1, 2],
    ]
    ans2 = 3

    m3 = [
        [1, 2],
        [100, 150],
        [300, 20],
    ]
    ans3 = 122

    m4 = [[4, 0, 3], [8, 3, 8], [4, 5, 0], [3, 4, 4], [8, 8, 0]]
    ans4 = 9

    for _ in range(5000):
        check(solution(m1), ans1)
        check(solution(m2), ans2)
        check(solution(m3), ans3)
        check(solution(m4), ans4)
