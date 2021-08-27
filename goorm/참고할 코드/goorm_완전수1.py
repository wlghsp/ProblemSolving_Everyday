import sys

input = lambda: sys.stdin.readline().rstrip()


a, b = map(int, input().split())


for i in range(a, b + 1):
    sumofdivisors = 0
    for j in range(1, i):
        if i % j == 0:
            sumofdivisors += j
    if sumofdivisors == i:
        print(i, end=" ")
