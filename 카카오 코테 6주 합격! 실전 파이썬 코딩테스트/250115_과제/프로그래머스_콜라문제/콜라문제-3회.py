import sys

sys.setrecursionlimit(10 ** 6)

def solution(a, b, n):
    def recur(total, cnt):
        if total < a:
            return cnt
        else:
            return recur((total // a) * b + (total % a), cnt + (total // a) * b)

    return recur(n, 0)


print(solution(3, 1, 20))