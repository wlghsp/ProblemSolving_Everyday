def solution(park, routes):
    N, M = len(park), len(park[0])
    direction = {'N': (-1, 0),'S': (1, 0),'W': (0, -1),'E': (0, 1)}

    cur_x, cur_y = 0, 0
    # 시작 위치 찾기
    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                cur_x, cur_y = i, j
                break
    # 명령어 처리
    for r in routes:
        d, dist = r.split()
        dx, dy = direction[d]
        nx, ny = cur_x, cur_y

        for _ in range(int(dist)):
            nx += dx
            ny += dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M or park[nx][ny] == 'X':
                break
        else: # for-else 문
            # break 없이 위의 반복문이 종료된 경우 실행 = 도착했다는 의미로 위치 변경
            cur_x, cur_y = nx, ny

    return [cur_x, cur_y]


print(solution(
    ["SOO", "OOO", "OOO"],
    ["E 2", "S 2", "W 1"]
))  # [2,1]
print(solution(
    ["SOO","OXX","OOO"],
    ["E 2","S 2","W 1"]
))  # [0,1]
print(solution(
    ["OSO","OOO","OXO","OOO"],
    ["E 2", "S 3", "W 1"]
))  # [0,0]
