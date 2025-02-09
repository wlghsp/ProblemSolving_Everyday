from collections import deque


def solution(queue1, queue2):
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    dq1, dq2 = deque(queue1), deque(queue2)
    length = len(queue1) + len(queue2)

    cnt = 0
    while cnt <= length * 2:
        if q1_sum == q2_sum:
            return cnt
        elif q1_sum < q2_sum: # 2번 큐의 합이 더 큰 경우
            # 2번 디큐에서 빼고
            popped2 = dq2.popleft()
            q2_sum -= popped2

            # 1번 디큐에 넣기
            dq1.append(popped2)
            q1_sum += popped2
        else: # 1번 큐의 합이 더 큰 경우
            # 1번 디큐에서 빼고
            popped1 = dq1.popleft()
            q1_sum -= popped1

            # 2번 디큐에 넣기
            dq2.append(popped1)
            q2_sum += popped1

        cnt += 1
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2