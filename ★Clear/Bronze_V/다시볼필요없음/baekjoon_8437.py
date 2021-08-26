import sys

input = sys.stdin.readline


num_of_apple = int(input())
gap = int(input())

natalia = (num_of_apple - gap) // 2

print(num_of_apple - natalia)
print(natalia)
