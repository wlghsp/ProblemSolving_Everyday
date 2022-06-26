import sys

input = lambda: sys.stdin.readline().rstrip()


def solve(arr: list) -> list:

    for i in range(len(arr)):
        target = arr[i]

        j = i - 1
        while j >= 0 and target < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j + 1] = target

    return arr


N = int(input())
arr = list(map(int, input().split()))
print(*solve(arr))
