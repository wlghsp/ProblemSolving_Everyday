def solution(board, skill):
    N, M = len(board), len(board[0])
    effect = [[0] * (M + 1) for _ in range(N + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            effect[r1][c1] -= degree
            effect[r2 + 1][c1] += degree
            effect[r1][c2 + 1] += degree
            effect[r2 + 1][c2 + 1] -= degree
        else:
            effect[r1][c1] += degree
            effect[r1][c2 + 1] -= degree
            effect[r2 + 1][c2 + 1] += degree
            effect[r2 + 1][c1] -= degree

    # 가로 누적합
    for x in range(N + 1):
        for y in range(1, M + 1):
            effect[x][y] += effect[x][y - 1]

    # 세로 누적합
    for x in range(1, N + 1):
        for y in range(M + 1):
            effect[x][y] += effect[x - 1][y]

    # 원본 배열 반영
    for x in range(N):
        for y in range(M):
            board[x][y] += effect[x][y]

    # 최종 결과 계산
    answer = 0
    for i in range(N):
        for j in range(M):
            answer += 1 if board[i][j] > 0 else 0
    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
               , [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])) # 10

print(solution([[1,2,3],[4,5,6],[7,8,9]],
               [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])) # 6