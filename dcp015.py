import random
from typing import Generator
"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory,
pick a random element from the stream with uniform probability.
"""


def stream(n: int) -> Generator[int, None, None]:
    for i in range(1, n + 1):
        yield i


def solution(stream: Generator[int, None, None]):
    num_samples: int = 0
    picked: int = -1

    for sample in stream:
        num_samples += 1
        picked = sample if random.random() <= 1.0 / num_samples else picked
    return picked


if __name__ == "__main__":
    results = []
    for i in range(1000):
        results.append(solution(stream(10)))
    print(sum(results) / 1000)
