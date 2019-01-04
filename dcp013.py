from typing import Tuple
"""
This problem was asked by Amazon.
Given an integer k and a string s,
find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2,
the longest substring with k distinct characters is "bcb".
"""

MAX_CHARS = 26


def isValid(count, k):
    val = 0
    for i in range(MAX_CHARS):
        if count[i] > 0:
            val += 1

    return (k >= val)


def lcs(s, k):
    u = 0
    n = len(s)

    curr_start = 0
    curr_end = 0
    max_window_size = 1
    max_window_start = 0

    count = [0] * MAX_CHARS

    count[ord(s[0]) - ord('a')] += 1
    for i in range(1, n):

        count[ord(s[i]) - ord('a')] += 1
        curr_end += 1

        while not isValid(count, k):
            count[ord(s[curr_start]) - ord('a')] -= 1
            curr_start += 1

        if curr_end - curr_start + 1 > max_window_size:
            max_window_size = curr_end - curr_start + 1
            max_window_start = curr_start

    return s[max_window_start:], max_window_size


def cdr(l: Tuple[str, int]) -> int:
    return l[1]


def check(actual: int, expected: int):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    check(cdr(lcs("aaaaaa", 4)), 6)
    check(cdr(lcs("aabbcc", 2)), 4)
    check(cdr(lcs("abbb", 1)), 3)
    check(cdr(lcs("aabacbebebe", 3)), 7)
