import sys

sys.setrecursionlimit(10 ** 6)

def solution(a, b, n):

    def recur(n, cnt):
        if n < a:
            return cnt

        return recur((n // a) * b + (n % a), cnt + (b * (n // a)))

    return recur(n, 0)


print(solution(3, 1, 20)) # 9