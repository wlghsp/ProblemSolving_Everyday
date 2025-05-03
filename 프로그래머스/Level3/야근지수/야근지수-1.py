import heapq


def solution(n, works):
    max_heap = []
    for w in works:
        heapq.heappush(max_heap, (-w, w))
    while n > 0:
        _, w = heapq.heappop(max_heap)
        if w > 0:
            w -= 1
        heapq.heappush(max_heap, (-w, w))
        n -= 1

    return sum(i ** 2 for _, i in max_heap)

print(solution(4, [4, 3, 3])) # 12
print(solution(3, [1, 1])) # 0
