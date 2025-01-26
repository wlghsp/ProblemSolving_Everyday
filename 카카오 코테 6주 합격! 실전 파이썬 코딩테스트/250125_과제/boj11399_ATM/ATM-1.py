N = int(input())
P = list(map(int, input().split()))
P.sort()

res = 0
for i in range(len(P)):
    person = 0
    for j in range(i + 1):
        person += P[j]
    res += person
print(res)