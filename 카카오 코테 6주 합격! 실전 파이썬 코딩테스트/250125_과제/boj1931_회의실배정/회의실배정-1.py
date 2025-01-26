import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
current = 0
for start, end in meetings:
    if start >= current:
        cnt += 1
        current = end
print(cnt)