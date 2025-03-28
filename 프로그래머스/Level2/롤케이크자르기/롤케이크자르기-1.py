from collections import defaultdict

def solution(topping):
    answer = 0
    left, right = defaultdict(int), defaultdict(int)
    left[topping[0]] += 1
    for i in range(1, len(topping)):
        right[topping[i]] += 1
    if check_keys(left, right):
        answer += 1

    for i in range(1, len(topping) - 1):
        left[topping[i]] += 1
        right[topping[i]] -= 1

        if right[topping[i]] == 0:
            right.pop(topping[i])

        if check_keys(left, right):
            answer += 1


    return answer

def check_keys(left, right):
    return len(left.keys()) == len(right.keys())


print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0