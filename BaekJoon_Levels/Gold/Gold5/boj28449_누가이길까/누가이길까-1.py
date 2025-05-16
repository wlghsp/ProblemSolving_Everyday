
def lower_bound(arr, target):
    l, r = 0, len(arr)

    while l < r:
        mid = l + (r - l) // 2

        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


def upper_bound(arr, target):
    l, r = 0, len(arr)

    while l < r:
        mid = l + (r - l) // 2

        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return l

N, M = map(int, input().split())
HI = list(map(int, input().split()))
ARC = list(map(int, input().split()))
ARC.sort()

result = [0, 0, 0]
for h in HI:
    win = lower_bound(ARC, h)
    lose = M - upper_bound(ARC, h)
    draw = upper_bound(ARC, h) - win

    result[0] += win
    result[1] += lose
    result[2] += draw

print(*result, sep=' ')
