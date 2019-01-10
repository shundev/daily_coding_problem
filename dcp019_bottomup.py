from typing import List


def solution(matrix: List[List[int]]) -> int:
    k = len(matrix[0])
    best_cost = [0] * k
    for cost in matrix:
        temp_cost = [0] * k
        for index in range(k):
            temp_cost[index] = cost[index] + min(best_cost[:index] +
                                                 best_cost[index + 1:])
        best_cost = temp_cost

    return min(best_cost)


def check(actual: int, expected: int):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    m1 = [[1, 2]]
    ans1 = 1

    m2 = [
        [1, 2],
        [1, 2],
    ]
    ans2 = 3

    m3 = [
        [1, 2],
        [100, 150],
        [300, 20],
    ]
    ans3 = 122

    m4 = [[4, 0, 3], [8, 3, 8], [4, 5, 0], [3, 4, 4], [8, 8, 0]]
    ans4 = 9

    check(solution(m1), ans1)
    check(solution(m2), ans2)
    check(solution(m3), ans3)
    check(solution(m4), ans4)
