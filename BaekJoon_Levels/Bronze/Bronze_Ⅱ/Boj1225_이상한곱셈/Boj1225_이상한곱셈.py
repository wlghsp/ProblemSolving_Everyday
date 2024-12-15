import sys

input = lambda: sys.stdin.readline().rstrip()

a, b = input().split()
sum_a = sum(map(int, a))
result = 0

for i in b:
    result += sum_a * int(i)

print(result)
