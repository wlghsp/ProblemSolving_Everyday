

import heapq


h = []


heapq.heappush(h, 7)
heapq.heappush(h, 5)
heapq.heappush(h, 2)

while len(h):
    print(heapq.heappop(h))
