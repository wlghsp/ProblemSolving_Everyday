from collections import deque

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
odd_even_dir = [[0, 2, 4, 6], [1, 3, 5, 7]]

N, M, K = map(int, input().split())
grid = [[0] * N for _ in range(N)]
fireball_info = [list(map(int, input().split())) for _ in range(M)]
fireball_dict = {(r, c): deque() for r in range(N) for c in range(N)}
for r, c, m, s, d in fireball_info:
    fireball_dict[(r - 1, c - 1)].append([m, s, d])

for _ in range(K):
    # 1. 파이어볼 이동 d 방향 s 만큼 이동
    new_fireballs = []
    for k in fireball_dict.keys():

        fireballs = fireball_dict[(k[0], k[1])]
        while fireballs:
            m, s, d = fireballs.popleft()
            if m == 0: continue
            nr, nc = (k[0] + dir[d][0] * s) % N, (k[1] + dir[d][1] * s) % N
            new_fireballs.append((nr, nc, m, s, d))

    for r, c, m, s, d in new_fireballs:
        fireball_dict[(r, c)].append((m, s, d))

    # 2. 파이어볼 2개 이상인 칸 처리
    for k, fireballs in fireball_dict.items():
        if len(fireballs) >= 2:
            tm, ts, tf = 0, 0, len(fireballs)
            odd_cnt, even_cnt = 0, 0
            for _ in range(tf):
                m, s, d = fireballs.popleft()
                tm += m
                ts += s
                if d % 2 == 0:
                    even_cnt += 1
                else:
                    odd_cnt += 1
            direction = []
            if odd_cnt == tf or even_cnt == tf:
                direction = odd_even_dir[0]
            else:
                direction = odd_even_dir[1]
            # 4방향 파이어볼 생성
            for d in direction:
                fireball_dict[(k[0], k[1])].append((tm // 5, ts // tf, d))

# 3. 파이어볼 질량의 합 처리
result = 0
for balls in fireball_dict.values():
    for fire in balls:
        result += fire[0]
print(result)
