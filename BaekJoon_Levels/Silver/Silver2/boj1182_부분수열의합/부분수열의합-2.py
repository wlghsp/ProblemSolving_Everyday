
N, S = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
def recur(picked, start):
    global ans
    if picked and sum(picked) == S:
        ans += 1

    for i in range(start, N):
        picked.append(nums[i])
        recur(picked, i + 1)
        picked.pop()

recur([], 0)

print(ans)