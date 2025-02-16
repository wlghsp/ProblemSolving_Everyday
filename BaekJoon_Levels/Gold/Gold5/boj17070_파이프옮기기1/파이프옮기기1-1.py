"""
파이프 최소 위치 (0, 0), (0, 1) = 이 위치는 항상 0 이다.

1 = 벽, 0 = 빈칸

파이프 밀 수 있는 방향 3 가지 , 오른쪽 , 오른쪽 대각선 45도 아래, 아래
대각선, 좌, 아래
파이프의 상태 파악 필요
이동 방법
가로 - 2가지, 세로 - 2가지, 대각선 - 3가지


"""
import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
move_counts = [[0] * N for _ in range(N)]
pipe_loc = ((0, 0), (0, 1))
dp = [[0] * N for _ in range(N)]

def dfs(loc):
    pass

print(dp[N][N])






