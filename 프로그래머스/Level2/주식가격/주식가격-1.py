from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    q = deque([i for i in range(len(prices))])
    idx = 0
    while q and idx < len(prices) - 1:
        p = q.popleft()
        i = 0
        while i < len(q) - 1 and prices[p] <= prices[q[i]]:
            i += 1

        answer[idx] = q[i] - p
        idx += 1

    return answer


print(solution([1, 2, 3, 2, 3])) # 	[4, 3, 1, 1, 0]