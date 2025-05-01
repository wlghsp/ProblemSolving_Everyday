D = int(input())
N = int(input())
records = [0] * (D + 2)
visitors = [0] * (D + 2)

for _ in range(N):
    a, b = map(int, input().split())
    records[a] += 1
    records[b + 1] -= 1

for i in range(1, D + 1):
    visitors[i] = visitors[i - 1] + records[i]

for i in range(1, D + 1):
    print(visitors[i])
