import sys

input = lambda: sys.stdin.readline().rstrip()


def solve(board, moves):
    answer = 0
    stk = []
    for pos in moves:
        for i in range(len(board)):
            if board[i][pos - 1] != 0:
                tmp = board[i][pos - 1]
                board[i][pos - 1] = 0
                if stk and tmp == stk[-1]:
                    answer += 2
                    stk.pop()
                else: stk.append(tmp)

                break
    return answer

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
moves = list(map(int, input().split()))
print(solve(board, moves))

