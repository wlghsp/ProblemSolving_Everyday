N, M = map(int, input().split())
heights = list(map(int, input().split()))

def is_possible(target):
    res = 0
    for h in heights:
        if h > target:
            res += h - target
    return res >= M


l, r = 1, max(heights)
max_heights = 0
while l <= r:
    mid = l + (r - l) // 2

    if is_possible(mid):
        max_heights = mid
        l = mid + 1
    else:
        r = mid - 1

print(max_heights)
