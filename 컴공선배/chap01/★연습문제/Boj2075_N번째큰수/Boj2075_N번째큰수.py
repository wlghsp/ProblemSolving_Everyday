
import sys

input = lambda : sys.stdin.readline().rstrip()
import heapq
n = int(input())
hq = []
for _ in range(n):
    for r in map(int,input().split()):
        if len(hq) >= n:
            heapq.heappushpop(hq, r)
        else:
            heapq.heappush(hq, r)

print(heapq.heappop(hq))