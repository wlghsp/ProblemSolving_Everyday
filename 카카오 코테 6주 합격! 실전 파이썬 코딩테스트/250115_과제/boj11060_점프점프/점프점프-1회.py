from collections import deque

N = int(input())
arr = list(map(int, input().split()))

dq = deque([0])
jump_count = [-1] * (N + 1)
jump_count[0] = 0

while dq:
    p_num = dq.popleft()

    for i in range(p_num, p_num + arr[p_num] + 1):
        if i > (N - 1): continue
        if jump_count[i] != -1: continue

        jump_count[i] = jump_count[p_num] + 1
        dq.append(i)

print(jump_count[N - 1])