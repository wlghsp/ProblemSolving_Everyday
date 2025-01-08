
def solution(num):

    def recur(n, cnt):
        if n == 1:
            return cnt

        if cnt >= 500:
            return -1

        if n % 2 == 0:
            return recur(n // 2, cnt + 1)
        else:
            return recur(n * 3 + 1, cnt + 1)

    return recur(num, 0)

print(solution(6)) # 8
print(solution(626331)) # -1