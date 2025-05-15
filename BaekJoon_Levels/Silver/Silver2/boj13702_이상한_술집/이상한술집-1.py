
N, K = map(int, input().split())
volumes = [int(input()) for _ in range(N)]

max_vol = 0
l, r = 1, max(volumes)

def is_possible(target):
    cnt = 0
    for v in volumes:
        cnt += v // target
    return cnt >= K

while l <= r:
    mid = l + (r - l) // 2

    if is_possible(mid):
        max_vol = mid
        l = mid + 1
    else:
        r = mid - 1

print(max_vol)