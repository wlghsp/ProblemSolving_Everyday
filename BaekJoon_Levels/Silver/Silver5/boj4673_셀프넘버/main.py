import sys

input = lambda: sys.stdin.readline().rstrip()


def d(n):
    result = n
    while n > 0:
        result += n % 10
        n = n // 10
    return result

MAX_NUM = 10000
generated_numbers = set()

for i in range(1, MAX_NUM + 1):
    generated_numbers.add(d(i))


for i in range(1, MAX_NUM + 1):
    if i not in generated_numbers:
        print(i)