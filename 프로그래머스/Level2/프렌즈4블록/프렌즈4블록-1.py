def solution(m, n, board):
    answer = 0
    l_board = []
    for i in range(m):
        l_board.append(list(board[i]))

    def find_delete():
        delete_loc = set()
        for i in range(m - 1):
            for j in range(n - 1):
                block = l_board[i][j]
                if block == '0': continue

                if block == l_board[i + 1][j] == l_board[i][j + 1] == l_board[i + 1][j + 1]:
                    delete_loc.update({(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)})

        return delete_loc

    while True:
        to_delete = find_delete()

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

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 15

