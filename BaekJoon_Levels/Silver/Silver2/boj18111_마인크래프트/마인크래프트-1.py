import sys

input = lambda: sys.stdin.readline().rstrip()

N, M, B = map(int, input().split())
heights = []
for _ in range(N):
    heights += list(map(int, input().split()))

answers = []

for candidate in range(257):
    time, inventory = 0, B
    for curr in heights:
        if curr > candidate:
            diff = curr - candidate
            inventory += diff
            time += diff * 2
        elif curr < candidate:
            diff = candidate - curr
            inventory -= diff
            time += diff

    if inventory >= 0:
        answers.append((time, candidate))

answers.sort(key= lambda x: (x[0], -x[1]))
print(answers[0][0], answers[0][1])