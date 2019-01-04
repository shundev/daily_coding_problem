from dataclasses import dataclass
from random import random
import math
"""
This problem was asked by Google.

The area of a circle is defined as πr^2.
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Circle:
    center: Point
    r: float


def solve():
    num_points = 300000
    points = [Point(random(), random()) for i in range(num_points)]
    circle = Circle(Point(0, 0), 1)

    area_of_square = (circle.r * 2)**2
    area_of_circle = area_of_square * len(
        list(filter(lambda p: in_circle(p, circle), points))) / num_points
    pi = area_of_circle / (circle.r**2)
    return pi


def in_circle(p: Point, circle: Circle):
    x_2 = (p.x - circle.center.x)**2
    y_2 = (p.y - circle.center.y)**2
    return math.sqrt(x_2 + y_2) <= circle.r


def check(actual: bool, expected: bool):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    circle = Circle(Point(0, 0), 1)

    p0 = Point(0, 0)
    p1 = Point(-0.5, -0.5)
    p2 = Point(math.cos(math.pi / 3), math.sin(math.pi / 3))
    p3 = Point(-1, -1)
    p4 = Point(-2, 1)

    check(in_circle(p0, circle), True)
    check(in_circle(p1, circle), True)
    check(in_circle(p2, circle), True)
    check(in_circle(p3, circle), False)
    check(in_circle(p4, circle), False)

    print("-----")

    epsilon = 0.001

    check(solve() - 3.141 < epsilon, True)
    check(solve() - 3.141 < epsilon, True)
    check(solve() - 3.141 < epsilon, True)
    check(solve() - 3.141 < epsilon, True)
