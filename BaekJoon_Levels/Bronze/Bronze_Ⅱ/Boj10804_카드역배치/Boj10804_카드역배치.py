import sys

input = lambda: sys.stdin.readline().rstrip()

cards = [i for i in range(1, 21)]

def desc(a, b):
    part = cards[a-1: b]
    j = a-1
    for i in range(len(part)-1, -1, -1):
        cards[j] = part[i]
        j += 1

for _ in range(10):
    a, b = map(int, input().split())
    desc(a, b)

print(*cards)