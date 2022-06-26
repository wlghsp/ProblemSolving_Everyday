import sys

input = lambda: sys.stdin.readline().rstrip()


def solve(arr: list) -> list:
    for i in range(len(arr) - 1):
        min_index = i

        # 최솟값을 가진 인덱스 찾기, i 다음부터 끝까지 탐색
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


N = int(input())
arr = [i for i in map(int, input().split())]

print(*solve(arr))
