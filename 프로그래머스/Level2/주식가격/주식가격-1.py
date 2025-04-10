from collections import deque


def solution(prices):
    queue = deque()
    answer = [0] * len(prices)

    for i in range(len(prices)):
        cur = prices[i]

        while queue and cur < prices[queue[-1]]:
            prev_idx = queue.pop()
            answer[prev_idx] = i - prev_idx

        queue.append(i)

    for i in queue:
        answer[i] = len(prices) - 1 - i

    return answer


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
