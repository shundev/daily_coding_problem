# coding: utf-8

def solve(arr: [int], target: int) -> bool:
    for i, e in enumerate(arr):
        for j in range(i, len(arr)):
            if e + arr[j] == target:
                return True
            
    return False



if __name__ == "__main__":
    ans = solve([10, 1, 2, 7], 17)
    print(ans)
