import sys

input = lambda: sys.stdin.readline().rstrip()


def solve(arr: list) -> list:
    for i in range(1, len(arr)):

        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


N = int(input())
arr = list(map(int, input().split()))
print(*solve(arr))
