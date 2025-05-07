N = int(input())
nums = list(map(int, input().split()))
left, right = 0, N - 1
res = float('inf')
answer = [0] * 2
while left < right:
    total = nums[left] + nums[right]

    if abs(total) < res:
        res = abs(total)
        answer[0] = nums[left]
        answer[1] = nums[right]

    if total > 0:
        right -= 1
    elif total < 0:
        left += 1
    else:
        right -= 1
        left += 1
print(answer[0], answer[1])

