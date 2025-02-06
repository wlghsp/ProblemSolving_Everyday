N, M = map(int, input().split())
weights = list(map(int, input().split()))

if N == 0:
    print(0)
else:
    box_cnt = 1
    cur_box = 0
    for w in weights:
        if cur_box + w > M:
            box_cnt += 1
            cur_box = w
        else:
            cur_box += w
    print(box_cnt)