import sys

input = lambda: sys.stdin.readline().rstrip()


a, b = map(int, input().split())

sumofnums = 0


for i in range(a, b + 1):
    if i % 2 != 0:
        sumofnums += i
print(sumofnums)
