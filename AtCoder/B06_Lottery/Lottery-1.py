
N = int(input())
result = [0] + list(map(int, input().split()))
Q = int(input())
win_cnt = [0] * (N + 1)
lose_cnt = [0] * (N + 1)

for i in range(1, N + 1):
    win_cnt[i] += win_cnt[i - 1] + (1 if result[i] == 1 else 0)
    lose_cnt[i] += lose_cnt[i - 1] + (0 if result[i] == 1 else 1)

for _ in range(Q):
    a, b = map(int, input().split())
    win = win_cnt[b] - win_cnt[a - 1]
    lose = lose_cnt[b] - lose_cnt[a - 1]
    if win == lose:
        print("draw")
    elif win > lose:
        print("win")
    else:
        print("lose")