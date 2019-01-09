from typing import List, Generator
from collections import deque
"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space.
You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""


def solution(arr: List[int], k: int) -> Generator[int, None, None]:
    q: deque = deque()
    n = len(arr)

    for i in range(k):
        while q and arr[i] > arr[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, n):
        yield arr[q[0]]

        if q[0] < i - k + 1:
            q.popleft()

        while q and arr[i] > arr[q[-1]]:
            q.pop()
        q.append(i)

    yield arr[q[0]]


def check(actual: List[int], expected: List[int]):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    array = [10, 5, 2, 7, 8, 7]
    answer = [10, 7, 8, 8]
    k = 3
    sol = [n for n in solution(array, k)]
    check(sol, answer)

    array = [10, 5, 2]
    answer = [10]
    k = 3
    sol = [n for n in solution(array, k)]
    check(sol, answer)

    array = [10, 5, 2]
    answer = [10, 5]
    k = 2
    sol = [n for n in solution(array, k)]
    check(sol, answer)
    pass
