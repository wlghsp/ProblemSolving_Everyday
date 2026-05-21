import heapq
import sys, os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')


N = int(input())
heap = []
dasom = int(input())
for _ in range(N - 1):
    heapq.heappush(heap, int(input()) * -1)

ans = 0
while heap and (heap[0] * -1) >= dasom:
    max_num = heapq.heappop(heap) * -1
    heapq.heappush(heap, (max_num - 1) * -1)
    dasom += 1
    ans += 1


print(ans)