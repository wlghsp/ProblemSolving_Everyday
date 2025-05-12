N, B, W = map(int, input().split())
rocks = list(input())

b_cnt, w_cnt = 0, 0
left = 0

max_length = 0
for right in range(N):
    if rocks[right] == 'B':
        b_cnt += 1
    else:
        w_cnt += 1

    while b_cnt > B:
        if rocks[left] == 'B':
            b_cnt -= 1
        else:
            w_cnt -= 1
        left += 1

    if w_cnt >= W:
        max_length = max(max_length, right - left + 1)

print(max_length)