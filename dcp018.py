from typing import List, Generator
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
    i = 0
    while i + k - 1 < len(arr):
        max_ = arr[i]
        for j in range(i + 1, i + k):
            if arr[j] > max_:
                max_ = arr[j]
        yield max_
        i += 1


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
