from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([(i, p) for i, p in enumerate(priorities)])

    while q:
        i, p = q.popleft()
        if any(v > p for i, v in q):
            q.append((i, p))
        else:
            answer += 1
            if i == location:
                return answer

    return answer


print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5