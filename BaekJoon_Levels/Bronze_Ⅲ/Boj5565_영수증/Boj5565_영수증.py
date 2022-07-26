import sys

input = lambda: sys.stdin.readline().rstrip()
total_p = int(input())
prices = []
for _ in range(9):
    prices.append(int(input()))

print(total_p - sum(prices))
