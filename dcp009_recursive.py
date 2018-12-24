"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def largest_sum(s: [int]) -> int:
  l = len(s)
  if l == 1:
    return s[0]
  if l == 2:
    return s[0] if s[0] > s[1] else s[1]
  if l == 3:
    take_none = largest_sum(s[2:])
    take_0 = s[0] + largest_sum(s[2:])
    take_1 = s[1]
    return max([take_none, take_0, take_1])
  take_none = largest_sum(s[2:])
  take_0 = s[0] + largest_sum(s[2:])
  take_1 = s[1] + largest_sum(s[3:])
  return max([take_none, take_0, take_1])


def check(act, exp):
  assert act == exp, "Expected {}, but got {}".format(exp, act)
  print("OK")


if __name__ == "__main__":
  check(largest_sum([1]), 1)
  check(largest_sum([0]), 0)
  check(largest_sum([-1]), -1)
  check(largest_sum([1, -1]), 1)
  check(largest_sum([1, -1, 1]), 2)
  check(largest_sum([1, -1, 1, 2]), 3)
  check(largest_sum([1, -1, 1, 2, 3]), 5)

  check(largest_sum([2, 4, 6, 2, 5]), 13)
  check(largest_sum([-2, -4, -6, -2, 1]), 1)
  check(largest_sum([5, 1, 1, 5]), 10)
