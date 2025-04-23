# 바텀업 풀이

W, H = map(int, input().split())

# k가 0=교차로 턴, 1= 연속, 2= 시작
dp = [[[[0 for _ in range(3)] for _ in range(3)] for _ in range(H)] for _ in range(W)]
# 동쪽, 북쪽
dir = [(1, 0), (0, 1)]
MOD = 100000
# 초기화
if W > 1: dp[1][0][0][1] = 1 # 동쪽
if H > 1: dp[0][1][1][1] = 1 # 북쪽


for x in range(W):
    for y in range(H):
        for d in range(2):
            for k in range(3):
                val = dp[x][y][d][k]
                if val == 0: continue
                for i in range(2): # 다음 방향
                    nx, ny = x + dir[i][0], y + dir[i][1]
                    if not (0 <= nx < W and 0 <= ny < H): continue

                    if k == 2 or d == i:
                        dp[nx][ny][i][1] = (dp[nx][ny][i][1] + val) % MOD
                    elif k == 1:
                        dp[nx][ny][i][0] = (dp[nx][ny][i][0] + val) % MOD
res = 0
for d in range(2):
    for k in range(2):
        res = (res + dp[W - 1][H - 1][d][k]) % MOD
print(res)