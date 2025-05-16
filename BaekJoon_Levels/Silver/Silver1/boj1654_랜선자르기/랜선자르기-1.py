K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

def is_possible(target):
    cnt = 0
    for l in lines:
        cnt += l // target
    return cnt >= N


l, r = 1, max(lines)
ans = 0
while l <= r:
    mid = l + (r - l) // 2
    if is_possible(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)