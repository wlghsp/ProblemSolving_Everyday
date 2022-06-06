import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = [i for i in map(int, input().split())]
answer, lt, total = 0, 0, 0

for rt in range(N):
    total += arr[rt]

    if total == M:
        answer += 1

    while total >= M: # 합이 M과 같아도 진행
        total -= arr[lt]
        lt += 1
        if total == M:
            answer += 1

print(answer)