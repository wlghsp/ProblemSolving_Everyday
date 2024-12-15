import sys

input = lambda: sys.stdin.readline().rstrip()

name = input().split("-")
result = ""
for n in name:
    result += n[0]
print(result)
