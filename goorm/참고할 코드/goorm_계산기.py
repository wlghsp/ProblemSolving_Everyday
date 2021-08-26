"""
10 + 5
15

10 - 5
5


switch문을 람다식으로 구현하여 향후 참고할 코드 
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def calculator(statement):
    return {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }[statement[1]](int(statement[0]), int(statement[2]))


s = input().split()
if s[1] == "/":
    print("%.2f" % calculator(s))
else:
    print(calculator(s))
