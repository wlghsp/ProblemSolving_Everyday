N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def recur(picked, start, length):
    global cnt
    if len(picked) == length:
        if sum(picked) == S:
            cnt += 1
        return

    for i in range(start, len(arr)):
        picked.append(arr[i])
        recur(picked, i + 1, length)
        picked.pop()

for i in range(1, N + 1):
    recur([], 0, i)

print(cnt)
