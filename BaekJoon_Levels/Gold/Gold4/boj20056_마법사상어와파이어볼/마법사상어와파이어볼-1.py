from collections import deque, defaultdict

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
odd_even_dir = [[0, 2, 4, 6], [1, 3, 5, 7]]

N, M, K = map(int, input().split())
grid = [[0] * N for _ in range(N)]
fireball_info = [list(map(int, input().split())) for _ in range(M)]
fireball_dict = defaultdict(deque)

# 초기 파이어볼 저장
for r, c, m, s, d in fireball_info:
    fireball_dict[(r - 1, c - 1)].append([m, s, d])

for _ in range(K):
    # 1. 파이어볼 이동 d 방향 s 만큼 이동
    new_fireball_dict = defaultdict(deque) # 영향을 주지 않기 위함

    for (r, c), fireballs in fireball_dict.items():
        while fireballs:
            m, s, d = fireballs.popleft()
            if m == 0: continue
            nr, nc = (r + dir[d][0] * s) % N, (c + dir[d][1] * s) % N
            new_fireball_dict[(nr, nc)].append((m, s, d))

    fireball_dict = new_fireball_dict

    # 2. 파이어볼 2개 이상인 칸 처리
    for (r, c), fireballs in fireball_dict.items():
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

            if tm // 5 > 0: # 질량 0이 되면 추가하지 않음
                direction = odd_even_dir[0] if odd_cnt == tf or even_cnt == tf else odd_even_dir[1]
                # 4방향 파이어볼 생성
                for d in direction:
                    fireball_dict[(r, c)].append((tm // 5, ts // tf, d))

# 3. 파이어볼 질량의 합 처리
print(sum(m for balls in fireball_dict.values() for m, _, _ in balls))
