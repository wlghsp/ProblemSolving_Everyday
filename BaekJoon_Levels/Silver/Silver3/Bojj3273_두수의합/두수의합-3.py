
N = int(input())
arr = list(map(int, input().split()))
X = int(input())
arr.sort()
left, right = 0, N - 1

ans = 0
while left < right:
    total = arr[left] + arr[right]

    if total < X:
        left += 1
    elif total > X:
        right -= 1
    else:
        ans += 1
        left += 1
        right -= 1

print(ans)
