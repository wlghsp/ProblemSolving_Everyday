
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

roads = [i for i in map(int, input().split())]
prices = [i for i in map(int, input().split())]

min_price = roads[0] * prices[0]
min_cost = prices[0]

for i in range(1, N-1):
    if min_cost > prices[i]:
        min_cost = prices[i]

    min_price += min_cost * roads[i]

print(min_price)