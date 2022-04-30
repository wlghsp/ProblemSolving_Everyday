import heapq

nums = [4,1,7,3,8,5]
heap = []


for num in nums:
    heapq.heappush(heap, (-num, num)) # (우선순위, 값) 큰값의 우선순위가 음수일 때 작으므로.

print(heap)

while heap:
    print(heapq.heappop(heap)[1])