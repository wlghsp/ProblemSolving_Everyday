
import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())


answer, lt, total = 0, 0, 0
M = (N//2) + 1
arr = [i+1 for i in range(M)]
for rt in range(M):
    total += arr[rt]

    if total == N:
        answer += 1

    while total >= N:
        total -= arr[lt]
        lt += 1
        if total == N:
            answer += 1

print(answer)