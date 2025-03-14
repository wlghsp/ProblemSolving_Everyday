from collections import deque

gears = [deque(input()) for _ in range(4)]
K = int(input())
rotate_method = [list(map(int, input().split())) for _ in range(K)]

for rotate_gear, direction in rotate_method:
    rotate_gear -= 1
    rotate_directions = [0] * 4
    rotate_directions[rotate_gear] = direction
    # 1. 왼쪽
    for i in range(rotate_gear, 0, -1):
        if gears[i - 1][2] != gears[i][6]:
            rotate_directions[i - 1] = -rotate_directions[i]
        else:
            break

    # 2. 오른쪽
    for i in range(rotate_gear, 3):
        if gears[i + 1][6] != gears[i][2]:
            rotate_directions[i + 1] = -rotate_directions[i]
        else:
            break

    for i in range(4):
        if rotate_directions[i] != 0:
            gears[i].rotate(rotate_directions[i])

print(sum((1 << i) for i in range(4) if gears[i][0] == '1' ))