import sys

input = sys.stdin.readline


bottles_of_sum = sum(list(map(int, input().split())))

print(bottles_of_sum * 5)
