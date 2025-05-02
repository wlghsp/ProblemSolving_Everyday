from heapq import heappush, heappop


def solution(operations):
    min_heap = []
    for op in operations:
        if op[0] == 'I':
            num = int(op[2:])
            heappush(min_heap, num)
        else:
            if min_heap:
                if op == 'D -1':
                    heappop(min_heap)
                else:
                    # 최댓값 삭제
                    min_heap.sort()
                    min_heap.pop()
    min_heap.sort()
    return [min_heap[-1], min_heap[0]] if min_heap else [0, 0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))  # [333,-45]
