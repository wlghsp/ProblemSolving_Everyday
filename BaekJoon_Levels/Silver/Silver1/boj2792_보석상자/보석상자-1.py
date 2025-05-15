import math

N, M = map(int, input().split())
jewel_cnt = [int(input()) for _ in range(M)]
min_jealousy = float('inf')

def is_possible(jealousy):
    cnt = 0
    for jewel in jewel_cnt:
        cnt += math.ceil(jewel / jealousy)

    return cnt <= N

l, r = 1, max(jewel_cnt)

while l <= r:
    mid = l + (r - l) // 2

    if is_possible(mid):
        min_jealousy = mid
        r = mid - 1
    else:
        l = mid + 1
print(min_jealousy)
