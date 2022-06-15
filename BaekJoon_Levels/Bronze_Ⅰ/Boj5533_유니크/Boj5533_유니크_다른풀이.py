import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

a = []
for i in range(n):
    a += [list(map(int, input().split()))]

# zip 함수 병렬 처리, 행열을 바꿈
now = list(zip(*a))
point = []
for i in range(n):
    cnt = 0
    for j in range(3):
        if now[j].count(now[j][i]) == 1:
            cnt += now [j][i]
    point.append(cnt)

for i in point:
    print(i)