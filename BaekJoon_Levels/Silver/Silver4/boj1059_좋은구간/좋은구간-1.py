L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.sort()

res = 0
end = S[0] - 1
start = 1

if n > end:
    for i in range(1, len(S)):
        if n < S[i]:
            end = S[i] - 1
            start = S[i - 1] + 1
            break

for i in range(start, end + 1):
    for j in range(i + 1, end + 1):
        if i <= n <= j:
            res += 1

print(res)
