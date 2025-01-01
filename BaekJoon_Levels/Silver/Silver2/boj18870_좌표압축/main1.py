

N = int(input())

arr = list(map(int, input().split()))
arr_no_redundancy = list(set(arr))
arr_no_redundancy.sort()

mapper = {}

for i, ele in enumerate(arr_no_redundancy):
    mapper[ele] = i

ans = [0] * N

for i, ele in enumerate(arr):
    ans[i] = mapper[ele]

print(*ans)