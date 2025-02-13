import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    heights.sort()
    new_heights = [0] * N
    l, r  = 0, N - 1
    i = 0
    while l <= r and i < N:
        new_heights[r] = heights[i]
        i += 1
        if i < N:
            new_heights[l] = heights[i]
            i += 1
        l += 1
        r -= 1

    max_difficulty = abs(new_heights[0] - new_heights[N - 1])
    for i in range(N - 1):
        max_difficulty = max(max_difficulty, abs(new_heights[i] - new_heights[i + 1]))

    print(max_difficulty)


