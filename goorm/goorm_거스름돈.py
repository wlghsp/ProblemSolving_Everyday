import sys

input = sys.stdin.readline


price = int(input())

coin_types = [500, 100, 50, 10]

coin_counts = []
rest = 1000 - price
for coin in coin_types:
    coin_counts.append(rest // coin)
    rest %= coin

print(*coin_counts, end="")
print(" ")
