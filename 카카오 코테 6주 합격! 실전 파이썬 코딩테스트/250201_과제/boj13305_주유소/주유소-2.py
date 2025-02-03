import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
dist = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_cost = 0
min_price= prices[0]
for i in range(len(dist)):
    if min_price > prices[i]:
        min_price = prices[i]
    min_cost += min_price * dist[i]

print(min_cost)