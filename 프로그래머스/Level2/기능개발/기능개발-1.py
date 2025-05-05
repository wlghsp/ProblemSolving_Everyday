import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    finish_time = deque()

    # 1. 100 % 까지 걸리는 기간 기록
    for progress, speed in zip(progresses, speeds):
        left = (100 - progress)
        days = math.ceil(left / speed)
        finish_time.append(days)

    # 2. 걸리는 시간으로 그룹별 카운트
    while finish_time:
        fun = finish_time.popleft()
        cnt = 1
        while finish_time and finish_time[0] <= fun:
            finish_time.popleft()
            cnt += 1
        answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]	)) # [1, 3, 2]