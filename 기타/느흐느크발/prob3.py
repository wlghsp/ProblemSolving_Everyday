

import sys
si = sys.stdin.readline
N, L, Q = map(int, si().split())
langs = [list(map(int, si().split()))[1:] for _ in range(N)]
lang_map = [[0 for _ in range(L)] for __ in range(N)]  # lang_map[i][l] := i번 사람이 l 번 언어를 아느냐?
for i in range(N):
    for l in langs[i]:
        lang_map[i][l - 1] = 1
# construct graph
INF = 100000000
con = [[INF for _ in range(N)] for __ in range(N)]
for i in range(N):
    con[i][i] = 0
    for j in range(i + 1, N):
        # i 라는 사람과 j 라는 사람이 대화가 가능하냐?
        for lang in range(L):
            if lang_map[i][lang] == 1 and lang_map[j][lang] == 1:
                con[i][j] = con[j][i] = 1
                break
# floyd-warshall algorithm
for k in range(N):
    for i in range(N):
        for j in range(N):
            if con[i][k] == INF or con[k][j] == INF: continue
            con[i][j] = min(con[i][j], con[i][k] + con[k][j])
for _ in range(Q):
    x, y = map(int, si().split())
    x -= 1
    y -= 1
    if con[x][y] == INF:
        print(-1)
    else:
        print(con[x][y] - 1)