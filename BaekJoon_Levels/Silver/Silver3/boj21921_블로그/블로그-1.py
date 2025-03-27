N, X = map(int, input().split())
visitor_cnt = list(map(int, input().split()))

# 슬라이딩 윈도우
sub_sum = sum(visitor_cnt[:X])
max_sum = sub_sum
max_cnt = 1

for i in range(X, N):
    sub_sum -= visitor_cnt[i - X]
    sub_sum += visitor_cnt[i]
    if max_sum < sub_sum:
        max_sum = sub_sum
        max_cnt = 1
    elif max_sum == sub_sum:
        max_cnt += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum, max_cnt, sep='\n')
