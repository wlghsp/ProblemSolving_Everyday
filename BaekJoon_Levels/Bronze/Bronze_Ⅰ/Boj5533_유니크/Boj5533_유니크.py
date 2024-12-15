import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
scores = []
players = [0] * N
for _ in range(N):
    scores.append(list(map(int, input().split())))
cols = []
for i in range(3):
    col = []
    for j in range(N):
        col.append(scores[j][i])
    cols.append(col)
for col in cols:
    for i in range(N):
        if col.count(col[i]) == 1:
            players[i] += col[i]
for p in players:
    print(p)
