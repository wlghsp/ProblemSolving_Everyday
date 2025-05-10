
T = int(input())
N = int(input())
record = [0] * (T + 1)

for i in range(N):
    L, R = map(int, input().split())
    record[L] += 1
    record[R] -= 1

employees = [0] * (T + 1)
employees[0] = record[0]
for i in range(1, T + 1):
    employees[i] = employees[i - 1] + record[i]

for i in employees[:T]:
    print(i)