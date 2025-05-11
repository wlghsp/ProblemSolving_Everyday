def solution(m, n, board):
    answer = 0
    l_board = []
    for b in board:
        l_board.append(list(b))
    def get_delete():
        delete_loc = set()
        for i in range(m - 1):
            for j in range(n - 1):
                cur = l_board[i][j]
                if cur == '0': continue

                if cur == l_board[i + 1][j] == l_board[i][j + 1] == l_board[i + 1][j + 1]:
                    delete_loc.update(((i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)))
        return delete_loc
    while True:
        to_delete = get_delete()

        if not to_delete:
            break

        answer += len(to_delete)

        for x, y in to_delete:
            l_board[x][y] = '0'

        for col in range(n):
            stack = []
            for row in range(m):
                if l_board[row][col] != '0':
                    stack.append(l_board[row][col])

            for row in range(m - 1, -1, -1):
                if stack:
                    l_board[row][col] = stack.pop()
                else:
                    l_board[row][col] = '0'

    return answer


print(solution(4, 5, 	["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 14