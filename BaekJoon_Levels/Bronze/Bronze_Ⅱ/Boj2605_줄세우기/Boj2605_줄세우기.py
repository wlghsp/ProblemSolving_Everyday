import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

arr = list(map(int, input().split()))
result = []
idx = 0
for i in range(1, n+1):
    result.insert(len(result) - arr[idx], i)
    idx += 1
print(*result)