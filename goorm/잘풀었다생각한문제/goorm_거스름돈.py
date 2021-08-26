"""
이코테 그리디에서 
거스름돈 문제와 거의 유사하게 문제 풀이함. 

문제는 쉽지만 
공부한 보람을 느껴서 좋았음
"""


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
