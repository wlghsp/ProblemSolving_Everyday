def solution(num):

    def recur(n, times):
        if n == 1:
            return times
        if times >= 500:
            return -1

        if n % 2 == 0:
            return recur(n // 2, times + 1)
        else:
            return recur(n * 3 + 1, times + 1)


    return recur(num , 0)

print(solution(6)) # 8