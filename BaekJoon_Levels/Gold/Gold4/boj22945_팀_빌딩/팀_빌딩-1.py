N = int(input())
ability = list(map(int, input().split()))

left, right = 0, N - 1
max_power = 0
while left < right:
    dist = right - left - 1
    power = min(ability[left], ability[right])
    max_power = max(max_power, dist * power)

    # 더 작은 쪽을 키워서 그 쪽 능력치를 키워야 최댓값을 찾을 수 있음
    if ability[left] < ability[right]:
        left += 1
    else:
        right -= 1

print(max_power)