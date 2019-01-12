from typing import List


def merge_sort(arr: List[int]):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    l_i = r_i = arr_i = 0

    while l_i < len(L) and r_i < len(R):
        if L[l_i] < R[r_i]:
            arr[arr_i] = L[l_i]
            l_i += 1
        else:
            arr[arr_i] = R[r_i]
            r_i += 1
        arr_i += 1

    while l_i < len(L):
        arr[arr_i] = L[l_i]
        l_i += 1
        arr_i += 1

    while r_i < len(R):
        arr[arr_i] = R[r_i]
        r_i += 1
        arr_i += 1


def check(actual: List[int], expected: List[int]):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    ans = sorted(arr)
    merge_sort(arr)
    check(arr, ans)
