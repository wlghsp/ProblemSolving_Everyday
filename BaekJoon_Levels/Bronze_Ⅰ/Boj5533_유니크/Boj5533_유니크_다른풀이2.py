import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
score = [[], [], []]
total = []

for i in range(n):
    a, b, c = map(int, input().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)
# 와 이렇게 넣는걸 생각 못했다.
# 그냥 빈 리스트를 만들어두고 각 리스트에 집어 넣음
# 행열 역전 이런거 할 생가도 안함.

for i in range(n):
    s_score = 0
    for j in range(3):
        if score[j].count(score[j][i]) == 1:
            s_score += score[j][i]
    total.append(s_score)

for i in total:
    print(i)