
N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
result = [0] * N

rank_map = {}
idx = 0
for i in range(N):
    if sorted_arr[i] not in rank_map:
        rank_map[sorted_arr[i]] = idx
        idx += 1

for i in range(N):
    print(rank_map[arr[i]], end=" ")
