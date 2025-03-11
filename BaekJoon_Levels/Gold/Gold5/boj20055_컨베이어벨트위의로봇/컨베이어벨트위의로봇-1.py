from collections import deque

N, K = map(int, input().split())
belts = list(map(int, input().split()))
robots = [0] * N
step = 0
while belts.count(0) < K:
    step += 1
    # 벨트, 로봇 이동
    belts = [belts[-1]] + belts[:-1]
    robots = [0] + robots[:-1]

    # 내리기
    robots[-1] = 0

    # 로봇 이동
    for i in range(N - 2, -1, -1):
        if robots[i] == 1 and robots[i + 1] == 0 and belts[i + 1] > 0:
            robots[i] = 0
            belts[i + 1] -= 1
            robots[i + 1] = 1

    # 내리기
    robots[-1] = 0

    if belts[0] > 0:
        belts[0] -= 1
        robots[0] = 1

print(step)