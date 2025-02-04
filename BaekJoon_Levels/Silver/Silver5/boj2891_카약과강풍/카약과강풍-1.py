N, S, R = map(int, input().split())
broken = list(map(int, input().split()))
brought = list(map(int, input().split()))
teams = [1] * N
for br in broken:
    teams[br - 1] -= 1
for kayak in brought:
    teams[kayak - 1] += 1

for i in range(N):
    if teams[i] == 0:
        if i - 1 > 0 and teams[i - 1] >= 2: # 앞쪽에 여유가 있다면
            teams[i - 1] -= 1
            teams[i] += 1
        elif i + 1 < N and teams[i + 1] >= 2: # 뒤쪽에 여유가 있다면
            teams[i + 1] -= 1
            teams[i] += 1
cnt = 0
for t in teams:
    if t == 0:
        cnt += 1

print(cnt)