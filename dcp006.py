"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def count(s: str) -> int:
  l = len(s)
  if l == 1:
    # 1 digit => 1 way（not starting with 0)
    return 1
  elif l == 2:
    # '1' for the case where every char is considered as a number.
    # numWays(s) returns 1 if 2-digit number is included in [1:26].
    return 1 + numWays(s)
  take_1 = numWays(s[:1]) * count(s[1:])
  take_2 = numWays(s[:2]) * count(s[2:])
  return take_1 + take_2


def numWays(s: str) -> int:
  num = int(s, 10)
  if 1 <= num and num <= 26: return 1
  return 0


def check(s: str, expected: int):
  assert count(s) == expected, "Expected {0} Actual {1}".format(expected, count(s))
  print("OK")

if __name__ == "__main__":
  check("1", 1)
  check("11", 2)
  check("91", 1)
  check("111", 3)
  check("1234", 3)
