def solution(queue1, queue2):
    que_sum = sum(queue1) + sum(queue2)
    if que_sum % 2 != 0:
        return -1
    target = que_sum // 2

    len_q = len(queue1)
    ans = 0
    start = 0
    end = len_q - 1

    cur = sum(queue1)
    queue3 = queue1 + queue2

    while cur != target:
        if cur < target:
            end += 1
            if end == len_q * 2:
                return -1
            cur += queue3[end]
        else:
            cur -= queue3[start]
            start += 1
        ans += 1

    return ans

print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2