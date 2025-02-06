import sys
from itertools import combinations

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
corridor = [input().split() for _ in range(N)]

empty_space = []
teachers = []
# 빈칸과 선생님 담기
for i in range(N):
    for j in range(N):
        if corridor[i][j] == 'T':
            teachers.append((i, j))
        elif corridor[i][j] == 'X':
            empty_space.append((i, j))

def can_avoid_detection():
    for x, y in teachers:
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x, y # 이동 탐색 후 매번 선생님의 원래 위치로 돌아 오도록 함
            while True:
                nx += dx
                ny += dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N: break
                if corridor[nx][ny] == 'O': break
                if corridor[nx][ny] == 'S': return False

    return True

can_avoid = False
for comb in combinations(empty_space, 3):
    for x, y in comb: # 1. 장애물 설치
        corridor[x][y] = 'O'
    if can_avoid_detection(): # 2.감시 피할 수 있지 여부 확인
        can_avoid = True
        break
    for x, y in comb: # 3. 설치된 장애물 원상복구
        corridor[x][y] = 'X'

print("YES" if can_avoid else "NO")