


N = int(input())
a = [0 for i in range(N+1)]
for i in range(2, N+1):
    a[i] = i


for i in range(2, N+1):
    if a[i] == 0: continue
    for j in range(2*i, N+1, i):
        a[j] = 0

cnt = 0
for i in range(2, N+1):
    if a[i] != 0: cnt += 1

print(cnt)


