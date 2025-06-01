import itertools
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, T = map(int, input().split())
homes = set()
for _ in range(n):
    a, b = map(int, input().split())
    homes.add((a, b))

# 중복 순열로 이동 좌표 생성해서 해당 좌표가 존재하는지 확인
# (0, 0) 은 이동하지 않으므로 제거
combs = [(dx, dy) for dx, dy in itertools.product([-2, -1, 0, 1, 2], repeat = 2) if not (dx == 0 and dy == 0)]

def bfs():
    q = deque([(0, 0, 0)])

    while q:
        x, y, cnt = q.popleft()

        if y == T:
            return cnt

        for dx, dy in combs:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in homes: continue

            # 사용된 좌표는 삭제
            homes.remove((nx, ny))
            q.append((nx, ny, cnt + 1))

    return -1

print(bfs())
