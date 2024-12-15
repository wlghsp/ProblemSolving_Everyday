import sys
input = lambda : sys.stdin.readline().rstrip()

x, y = map(int, input().split())


def rev(num):
    answer = 0
    while num != 0:
        answer = answer * 10 + num % 10
        num //= 10
    return answer

print(rev(rev(x) + rev(y)))

