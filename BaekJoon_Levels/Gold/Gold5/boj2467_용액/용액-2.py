N = int(input())
arr = list(map(int, input().split()))

l_ans, r_ans = 0, 0
left, right = 0, len(arr) - 1
min_diff = float('inf')

while left < right:
    mixed_val = arr[left] + arr[right]

    if abs(mixed_val) < min_diff:
        min_diff = abs(mixed_val)
        l_ans, r_ans = arr[left], arr[right]

    if mixed_val > 0:  # 1.합이 양수면 더 작은 값을 찾아야 하므로 right 감소
        right -= 1
    elif mixed_val < 0:  # 2. 합이 음수면 더 큰 값을 찾아야하므로 left 증가
        left += 1
    else:
        break

print(l_ans, r_ans)
