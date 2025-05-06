
N, K = map(int, input().split())
nums = list(map(int, input().split()))

answer = sum(nums[:K])
max_val = answer
for i in range(K, N):
    answer += nums[i] - nums[i - K]
    max_val = max(answer, max_val)

print(max_val)