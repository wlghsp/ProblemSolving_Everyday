import sys

si = sys.stdin.readline
N, Q, T = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(N)]


def push(num):
    if num <= N:  # upper side
        col = num - 1

        # drop check
        cnt = 0
        for row in range(N - 2, -1, -1):
            if a[row][col] == 0: break
            cnt += 1
        if cnt >= T:  # drop the last ball
            a[N - 1][col] = 0

        # push one step
        for row in range(N - 1, 0, -1):
            if a[row][col] == 1: continue
            a[row][col], a[row - 1][col] = a[row - 1][col], a[row][col]
    elif num <= N * 2:  # right side
        row = num - N - 1
        # drop check
        cnt = 0
        for col in range(1, N, 1):
            if a[row][col] == 0: break
            cnt += 1
        if cnt >= T:
            a[row][0] = 0

        # push one step
        for col in range(0, N - 1):
            if a[row][col] == 1: continue
            a[row][col], a[row][col + 1] = a[row][col + 1], a[row][col]

    elif num <= N * 3:  # lower side
        col = N - (num - N * 2)

        # drop check
        cnt = 0
        for row in range(1, N, 1):
            if a[row][col] == 0: break
            cnt += 1
        if cnt >= T:  # drop the last ball
            a[0][col] = 0

        # push one step
        for row in range(0, N - 1, 1):
            if a[row][col] == 1: continue
            a[row][col], a[row + 1][col] = a[row + 1][col], a[row][col]
    else:  # left side
        row = N - (num - N * 3)
        # drop check
        cnt = 0
        for col in range(N - 2, -1, -1):
            if a[row][col] == 0: break
            cnt += 1
        if cnt >= T:
            a[row][N - 1] = 0

        # push one step
        for col in range(N - 1, 0, -1):
            if a[row][col] == 1: continue
            a[row][col], a[row][col - 1] = a[row][col - 1], a[row][col]


for _ in range(Q):
    num = int(si())
    push(num)
for i in range(N):
    print(*a[i])
