N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

# 정렬
A.sort()

def does_meet_the_condition(picked):
    return L <= sum(picked) <= R and X <= abs(picked[-1] - picked[0])

ans = 0
def recur(picked, start):
    global ans

    if len(picked) > N:
        return

    if len(picked) >= 2:
        if does_meet_the_condition(picked):
            ans += 1

    for i in range(start, N):
        picked.append(A[i])
        recur(picked, i + 1)
        picked.pop()


recur([], 0)

print(ans)