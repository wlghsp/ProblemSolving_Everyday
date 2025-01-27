N = int(input())
times = list(map(int, input().split()))
times.sort()

res = 0
for i in range(N):
    each_one = times[i]
    for j in range(i):
        each_one += times[j]
    res += each_one

print(res)
