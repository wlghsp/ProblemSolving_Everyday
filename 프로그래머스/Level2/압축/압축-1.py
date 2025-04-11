import string
from collections import deque


def solution(msg):
    answer = []
    queue = deque(list(msg))
    dictionary = {alpha: i for alpha, i in zip(string.ascii_uppercase, range(1, 27))}
    next_no = 27

    def make_str(end):
        res = []
        for i in range(end + 1):
            res.append(queue[i])
        return ''.join(res)

    while queue:
        end = 0
        while end < len(queue) and dictionary.get(make_str(end)):
            end += 1

        ch = []
        for i in range(end):
            ch.append(queue.popleft())

        joined = ''.join(ch)
        answer.append(dictionary[joined])

        if queue:
            dictionary[joined + queue[0]] = next_no
            next_no += 1

    return answer


print(solution("KAKAO")) # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("ABABABABABABABAB")) # [1, 2, 27, 29, 28, 31, 30]
