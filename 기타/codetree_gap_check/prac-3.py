N = int(input())
Q = int(input())
commands = [(d, int(l)) for d, l in (input().split() for _ in range(Q))]

# Please write your code here.
visit_cnt = [[0] * N for _ in range(N)]
dir = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

cx, cy = 0, 0
for d, l in commands:

    for _ in range(l):
        nx, ny = cx + dir[d][0], cy  + dir[d][1]
        if not (0 <= nx < N and 0 <= ny < N): continue

        visit_cnt[nx][ny] += 1
        cx, cy = nx, ny


cnt = 0
for i in range(N):
    for j in range(N):
        if visit_cnt[i][j] >= 2:
            cnt += 1

print(cnt)
"""
3
3
S 2
N 1
E 1

1
"""