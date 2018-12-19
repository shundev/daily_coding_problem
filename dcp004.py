# coding: utf-8

"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""


def solve(data: [int]) -> int:
    data.sort()
    should = 1
    for n in data:
        if n <= 0:
            continue
        if n > should:
            break
        else:
            should += 1
        
    return should


def test():
    check(solve([1, 2, 3, 4]), 5)
    check(solve([3, 4, -1, 1]), 2)
    check(solve([1, 2, 0]), 3)


def check(actual, expected):
    assert actual == expected, "{0} expected, but got {1}".format(expected, actual)

if __name__ == "__main__":
    test()
