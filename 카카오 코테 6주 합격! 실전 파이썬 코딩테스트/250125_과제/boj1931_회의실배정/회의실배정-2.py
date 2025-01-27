import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
prev = 0
for start, end in meetings:
    if start >= prev:
        cnt += 1
        prev = end
print(cnt)