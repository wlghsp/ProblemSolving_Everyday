import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    def morethan_K(arr):
        for sco in scoville:
            if sco < K:
                return False
        return True
    succeeded = True
    while not morethan_K(scoville):
        if len(scoville) <= 1:
            succeeded = False
            break
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        created = first + (second * 2)
        heapq.heappush(scoville, created)
        answer += 1

    return answer if succeeded else -1


print(solution([1, 2, 3, 9, 10, 12], 7)) # 2