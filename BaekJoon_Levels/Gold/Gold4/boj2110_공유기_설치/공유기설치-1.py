N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

def can_install(distance):
    count = 1
    last = houses[0]
    for i in range(1, N):
        if houses[i] - last >= distance:
            count += 1
            last = houses[i]
        if count >= C:
            return True

    return False

ans = 0
l, r = 1, (houses[-1] - houses[0])
while l <= r:
    mid = l + (r - l) // 2

    if can_install(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)