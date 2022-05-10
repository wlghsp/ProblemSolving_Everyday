
N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer, cnt, lt = 0, 0, 0

for rt in range(len(arr)):
    if arr[rt] == 0: cnt += 1
    while cnt > K:
        if arr[lt] == 0: cnt -= 1
        lt += 1
    answer = max(answer, rt - lt + 1)

print(answer)

