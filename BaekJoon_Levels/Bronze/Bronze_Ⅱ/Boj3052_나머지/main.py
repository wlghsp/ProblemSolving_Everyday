import sys

input = sys.stdin.readline

s1 = set()

for _ in range(10):
    n = int(input()) % 42
    s1.add(n)

print(len(s1))

