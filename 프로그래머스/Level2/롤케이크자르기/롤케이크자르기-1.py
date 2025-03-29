from collections import defaultdict

def solution(topping):
    answer = 0
    left, right = defaultdict(int), defaultdict(int)
    for t in topping:
        right[t] += 1

    for i in range(len(topping) - 1):
        t = topping[i]
        left[t] += 1
        right[t] -= 1

        if right[t] == 0:
            right.pop(t)

        if len(left) == len(right):
            answer += 1

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0