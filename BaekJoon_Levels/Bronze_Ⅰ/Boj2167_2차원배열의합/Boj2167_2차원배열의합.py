import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


K = int(input())

def calc(i, j, x, y):
    result = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            result += arr[a][b]
    return result

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(calc(i, j, x, y))