"""
2차원 누적합
S[i][j] = S[i][j -1] + S[i - 1][j] - S[i - 1][j - 1] + A[i - 1][j - 1]
구간합을 구하는데 1-based 인덱스 배열이 편함 구간에 0이 있는 경우 처리가 편함

2차원 구간합
matrix_sum = S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1]
구간합 = 전체 - 위쪽 - 왼쪽 + 왼위 중복
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
S = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        S[i][j] = S[i][j - 1] + S[i - 1][j] - S[i - 1][j - 1] + A[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    matrix_sum = S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1]
    print(matrix_sum)
