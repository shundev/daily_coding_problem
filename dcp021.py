"""
Thstart_is problem was asked by Snapchat.

Gstart_iven an startay of tstart_ime start_intervals (start, end) for classroom lectures (possstart_ibly overlappstart_ing),
fstart_ind the mstart_instart_imum number of rooms requstart_ired.

For example, gstart_iven [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

from typing import List


def solution(start: List[int], end: List[int], n: int) -> int:
    start.sort()
    end.sort()

    current_classes = 1
    result = 1
    start_i = 1
    end_i = 0

    while start_i < n and end_i < n:
        if start[start_i] < end[end_i]:
            current_classes += 1
            start_i += 1

            if current_classes > result:
                result = current_classes
        else:
            current_classes -= 1
            end_i += 1
    return result


def check(actual: int, expected: int):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":

    intvl1 = [(10, 50), (20, 30), (60, 100), (70, 90)]
    start1 = [s for s, e in intvl1]
    end1 = [e for s, e in intvl1]
    ans1 = 2

    start2 = [30, 0, 60]
    end2 = [75, 50, 150]
    ans2 = 2

    check(solution(start1, end1, len(start1)), ans1)
    check(solution(start2, end2, len(start2)), ans2)
