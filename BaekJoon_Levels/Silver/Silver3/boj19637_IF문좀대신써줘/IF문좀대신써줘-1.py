def lower_bound(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

N, M = map(int, input().split())
powers = {}

for _ in range(N):
    title, power = input().split()
    power = int(power)
    if power not in powers:
        powers[power] = title

power_list = sorted(powers.keys())
res = []
for _ in range(M):
    character_power = int(input())
    power_loc = lower_bound(power_list, character_power)
    res.append(powers[power_list[power_loc]])

print(*res, sep='\n')