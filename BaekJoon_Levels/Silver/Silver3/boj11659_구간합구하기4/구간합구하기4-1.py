import sys

input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])