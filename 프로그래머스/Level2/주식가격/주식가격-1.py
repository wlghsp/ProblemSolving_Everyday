from collections import deque


def solution(prices):
    q = deque()
    answer = [0] * len(prices)
    return answer


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
