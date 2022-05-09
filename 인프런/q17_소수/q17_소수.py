

N = int(input())

# 강사님 풀이
a = [0 for i in range(N+1)]
ans = 0
for i in range(2, N+1):
    if a[i] == 0:
        ans +=1
        for j in range(i, N+1, i):
            a[j] = 1

print(ans)