

def solution(num):
    def recur(number, times):
        if number == 1:
            return times

        if times >= 500:
            return -1

        if number % 2 == 0:
            return recur(number // 2, times + 1)
        else:
            return recur(number * 3 + 1, times + 1)

    return recur(num, 0)



print(solution(6)) # 8