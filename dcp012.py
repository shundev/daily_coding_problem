from typing import List, Set
"""
This problem was asked by Amazon.
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X? For example,
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


def numWaysR(n: int) -> int:
    """
    Recursive approach
    """
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2

    step1 = numWays(n - 1)
    step2 = numWays(n - 2)
    return step1 + step2


def numWays(n: int) -> int:
    """
    Bottom up approach
    """
    steps: List[int] = [1, 1, 2]
    if n <= 2:
        return steps[n]

    for i in range(3, n + 1):
        steps.append(steps[i - 1] + steps[i - 2])
    return steps[n]


def numWaysG(n: int, x: Set[int]) -> int:
    """
    Generalized
    """
    if n == 0:
        return 1

    ret: int = 0
    for step in x:
        if n == step:
            ret += 1
        elif n < step:
            pass
        else:
            ret += numWaysG(n - step, x)
    return ret


def check(actual, expected):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    X1 = set([1, 2])
    check(numWaysG(0, X1), 1)
    check(numWaysG(1, X1), 1)
    check(numWaysG(2, X1), 2)
    check(numWaysG(3, X1), 3)
    check(numWaysG(4, X1), 5)

    X2 = set([1, 2, 3])
    check(numWaysG(0, X2), 1)
    check(numWaysG(1, X2), 1)
    check(numWaysG(2, X2), 2)
    check(numWaysG(3, X2), 4)
