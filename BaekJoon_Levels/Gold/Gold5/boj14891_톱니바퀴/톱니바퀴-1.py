from collections import deque

gears = [deque(input()) for _ in range(4)]
K = int(input())
rotate_method = [list(map(int, input().split())) for _ in range(K)]

for rotate_number, direction in rotate_method:
    rotate_number -= 1
    rotate_direction = [0] * 4
    rotate_direction[rotate_number] = direction

    # 왼쪽 기어들 확인 (현재 기어 -> 왼쪽)
    for i in range(rotate_number, 0, -1):
        if gears[i][6] != gears[i - 1][2]:  # 맞닿은 극이 다르면 회전
            rotate_direction[i - 1] = -rotate_direction[i]
        else:
            break  # 같은 극이면 전달되지 않음
    # 오른쪽 기어들 확인 (현재 기어 -> 오른쪽)
    for i in range(rotate_number, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotate_direction[i + 1] = -rotate_direction[i]
        else:
            break

    # 회전 적용
    for i in range(4):
        if rotate_direction[i] != 0:
            gears[i].rotate(rotate_direction[i])

print(sum((1 << i) if gears[i][0] == '1' else 0 for i in range(4)))
