def solution(numbers, target):
    answer = 0
    length = len(numbers)

    def calc(operators):
        result = 0
        for num, op in zip(numbers, operators):
            if op == '+':
                result += num
            else:
                result -= num
        return result

    def recur(picked):
        nonlocal answer
        if len(picked) == length:
            if calc(picked) == target:
                answer += 1
            return

        for op in ['+', '-']:
            picked.append(op)
            recur(picked)
            picked.pop()

    recur([])

    return answer

print(solution([1, 1, 1, 1, 1], 3)) # 5