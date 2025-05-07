N = int(input())
nums = list(map(int, input().split()))
X = int(input())

nums.sort()
ans = 0
l, r = 0, N - 1

while l < r:
    total = nums[l] + nums[r]

    if total == X:
        ans += 1
        l += 1
        r -= 1
    elif total > X:
        r -= 1
    elif total < X:
        l += 1


print(ans)