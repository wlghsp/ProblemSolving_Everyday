import sys

input = lambda: sys.stdin.readline().rstrip()


def solve(arr: list) -> list:
    for end in range(1, len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i - 1] > to_insert:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = to_insert

    return arr


N = int(input())
arr = list(map(int, input().split()))
print(*solve(arr))
