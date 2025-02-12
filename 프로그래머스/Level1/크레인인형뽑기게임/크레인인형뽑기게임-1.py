def solution(board, moves):
    answer = 0
    N = len(board)
    basket = []
    def append_basket(doll):
        nonlocal answer
        # 인덱스로 확인 전에 basket이 비었는지 확인 필수
        if basket and basket[-1] == doll:
            basket.pop()
            answer += 2
        else:
            basket.append(board[i][m - 1])

    for m in moves:
        for i in range(N):
            if board[i][m - 1] != 0:
                append_basket(board[i][m - 1])
                board[i][m - 1] = 0
                break
    return answer


print(solution(
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
[1,5,3,5,1,2,1,4]
)) # 4