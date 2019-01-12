"""
Thstart_is problem was asked by Snapchat.

Gstart_iven an startay of tstart_ime start_intervals (start, end) for classroom lectures (possstart_ibly overlappstart_ing),
fstart_ind the mstart_instart_imum number of rooms requstart_ired.

For example, gstart_iven [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

from typing import List, Tuple


def solution(intervals: List[Tuple[int, int]]) -> int:
    # False -> start, True -> end
    timeline: List[Tuple[int, bool]] = []
    for start, end in intervals:
        timeline.extend([(start, False), (end, True)])
    timeline.sort(key=lambda x: x[0])

    current_classes = 0
    max_classes = 0
    for _, is_end in timeline:
        current_classes += -1 if is_end else 1
        if current_classes > max_classes:
            max_classes = current_classes

    return max_classes


def check(actual: int, expected: int):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    interval1 = [(10, 50), (20, 30), (60, 100), (70, 90)]
    ans1 = 2
    interval2 = [(30, 57), (0, 50), (60, 150)]
    ans2 = 2
    interval3 = [(0, 50), (50, 100)]
    ans3 = 1
    interval4 = [(900, 910), (940, 1200), (950, 1120), (1100, 1130),
                 (1500, 1900), (1800, 2000)]
    ans4 = 3

    check(solution(interval1), ans1)
    check(solution(interval2), ans2)
    check(solution(interval3), ans3)
    check(solution(interval4), ans4)
