


def solution(numbers, target):
    global answer
    answer = 0
    def dfs(index, sum):
        global answer
        # 1. 탈출 조건
        if index == len(numbers):
            if sum == target:
                answer += 1
            return

        # 2. 수행 동작
        dfs(index + 1, sum + numbers[index])
        dfs(index + 1, sum - numbers[index])
    dfs(0, 0)

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))