def solution(numbers):
    answer = []
    stk = []
    for num in reversed(numbers):
        while stk and stk[-1] <= num:
            stk.pop()
        answer.append(stk[-1] if stk else -1)
        stk.append(num)

    return list(reversed(answer))

print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]